from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstDjango.views.home', name='home'),
	
	#estariamos llamando al localhost con r'^$'    
    url(r'^$', 'app.views.index', name='index'),
    url(r'^home$', 'app.views.home', name='home'),
    url(r'^listado$', 'app.views.lista', name='listado'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
