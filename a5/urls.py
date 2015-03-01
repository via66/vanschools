from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'a5.views.home', name='home'),
    url(r'^map/', include('datadisplay.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
