from django.contrib import admin

# Register your models here.
from himapp.models import State, City, Country, Category, Director, Company, Subcategory, DirectorCompany


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'din']

class DirectorCompanyAdmin(admin.StackedInline):
    model = DirectorCompany
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'created_date','cin']
    inlines = (DirectorCompanyAdmin,)

admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubCategoryAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Company, CompanyAdmin)