from django.conf.urls import patterns, include, url

from .api import CompanyAPI, DirectorAPI

urlpatterns = patterns('',

           url(r'^companyinfo/(?P<cin>[-\w]+)/$', CompanyAPI.as_view(), name='company-api'),
           url(r'^directorinfo/(?P<din>[-\w]+)/$', DirectorAPI.as_view(), name='director-api'),
)