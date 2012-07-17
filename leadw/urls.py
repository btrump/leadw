from django.conf.urls.defaults import * # import patterns, include, url
from montyhall.api import MontyHallResultResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

monty_hall_result_resource = MontyHallResultResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leadw.views.home', name='home'),
    # url(r'^leadw/', include('leadw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(monty_hall_result_resource.urls)),
)
