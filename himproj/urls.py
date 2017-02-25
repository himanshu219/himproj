from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'himproj.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('himapp.urls')),


)

