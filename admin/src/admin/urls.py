from django.conf.urls.defaults import *
#from books.views import current_datetime,holamundo,search,contact,add_publisher
from django.views.generic import list_detail
from books.models import Publisher,Book
from feeds import LatestEntries,LatestEntriesByCategory
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




publisher_info = {
"queryset" : Publisher.objects.all(),
"template_name" : "books/publisher.html",
"extra_context" : {"book_list" : Book.objects.all}
}

feeds = {
'latest': LatestEntries,
'categories': LatestEntriesByCategory,
}

urlpatterns = patterns('books.views',
    (r'^time/$', 'current_datetime'),
    (r'^search/$', 'search'),
    (r'^contact/$', 'contact'),
    (r'^add_publisher/$', 'add_publisher'),
    (r'^publishers/$', list_detail.object_list, publisher_info),
    (r'^books/(w+)/$', 'books_by_publisher'),
    (r'^authors/(?P<author_id>d+)/$', 'author_detail'),
    (r'^reporte/$', 'hello_pdf'),
    
    #(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict': feeds } ),

    #('^about/$', direct_to_template, {'template': 'about.html'}),
    #('^about/(w+)/$', about_pages),

    # Examples:
    
    # url(r'^$', 'admin.views.home', name='home'),
    # url(r'^admin/', include('admin.foo.urls')),

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

