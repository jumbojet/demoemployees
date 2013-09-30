from django.conf.urls import patterns, include, url
from demoapp.views import get_all_employees,get_employee_by_id,get_employee_search

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demoapp.views.home', name='home'),
    # url(r'^demoapp/', include('demoapp.foo.urls')),
    url(r'^employees/$',get_all_employees),
    url(r'^employees/empdetail$',get_employee_by_id),
    url(r'^employees/empsearch$',get_employee_search),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
