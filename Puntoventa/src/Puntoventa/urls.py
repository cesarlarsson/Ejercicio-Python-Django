from django.conf.urls import patterns, include, url
from django.contrib import admin
from producto.views import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('producto.views',
     (r'^$', 'index'),                  
    (r'^categoria/$', 'categoriaform'),
    (r'^producto/$', 'productoform'),                   
    # Examples:
    # url(r'^$', 'Puntoventa.views.home', name='home'),
    # url(r'^Puntoventa/', include('Puntoventa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)