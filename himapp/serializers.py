from rest_framework import serializers

from .models import City, State, Country, Category, Director, Company, Subcategory, DirectorCompany


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'model_number', 'model_name', 'selling_price')


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = State
        fields = ('id', 'model_number', 'model_name', 'selling_price')

class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()
    class Meta:
        model = City
        fields = ('id', 'model_number', 'model_name', 'selling_price')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'model_number', 'model_name', 'selling_price')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'model_number', 'model_name', 'selling_price')



class BasicDirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('din', 'name',)


class BasicCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('cin','company_name',)



class CompanyDirectorSerializer(serializers.HyperlinkedModelSerializer):
    company = BasicCompanySerializer(read_only=True)

    class Meta:
        model = DirectorCompany
        fields = ('company','appointment_date',)

    def to_representation(self, instance):
        data = super(CompanyDirectorSerializer, self).to_representation(instance)
        company = data.pop('company')
        if company:
            for k, v in company.items():
                data['company_' + k] = v
        return data

class DirectorSerializer(serializers.ModelSerializer):
    companies = CompanyDirectorSerializer(read_only=True, many=True, source='directorcompany_set')

    class Meta:
        model = Director
        fields = ('din', 'name','companies')




class DirectorCompanySerializer(serializers.HyperlinkedModelSerializer):
    director = BasicDirectorSerializer(read_only=True)

    class Meta:
        model = DirectorCompany
        fields = ('director','designation','appointment_date',)

    def to_representation(self, instance):
        data = super(DirectorCompanySerializer, self).to_representation(instance)
        director = data.pop('director')
        for k, v in director.items():
            data['director_' + k] = v
        return data


class CompanySerializer(serializers.ModelSerializer):
    directors = DirectorCompanySerializer(read_only=True, many=True, source='directorcompany_set')

    class Meta:
        model = Company
        fields = ('cin','company_name', 'status', 'address1', 'address2', 'full_address', 'city', 'pincode', 'type','authorised_capital', 'paidup_capital', 'incorporation_date', 'agm_date', 'balancesheet_date','directors')

    def to_representation(self, instance):
        #todo shift this to each entity serializer
        data = super(CompanySerializer, self).to_representation(instance)
        data.update({
            'city':instance.city.name,
            'state':instance.city.state.name,
            'country':instance.city.country.name,
            'subcategory':instance.subcategory.name,
            'category':instance.subcategory.category.name,
        })
        return data