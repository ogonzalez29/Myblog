from django.conf.urls import patterns, include, url
from blog.views import archive
from blog.views import contacto, gracias

urlpatterns = patterns('',
     url(r'^$', archive),
     url(r'^/contacto/', 'blog.views.contacto', name='contacto'),
     url(r'^/gracias/', 'blog.views.gracias', name='gracias'),
     url(r'^/contactomail/', 'blog.views.contactomail', name='contactomail'), 
     url(r'^/index/', 'blog.views.index', name="index"),                
)
