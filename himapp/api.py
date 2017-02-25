from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from models import Company, Director
from .serializers import CompanySerializer, DirectorSerializer

class CompanyAPI(RetrieveAPIView):
    lookup_field = 'cin'
    lookup_url_kwarg = 'cin'
    renderer_classes = (JSONRenderer,)
    queryset = Company.objects.all().select_related('city','subcategory__category','directorcompany_set')
    serializer_class = CompanySerializer



class DirectorAPI(RetrieveAPIView):
    lookup_field = 'din'
    lookup_url_kwarg = 'din'
    renderer_classes = (JSONRenderer,)
    queryset = Director.objects.all().select_related('directorcompany_set')
    serializer_class = DirectorSerializer
