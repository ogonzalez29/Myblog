from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'), 
    #url(r'^index/', index, name="index"),
    url(r'^$', include('blog.urls')),
    url(r'^myblog/blog', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),                  

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
