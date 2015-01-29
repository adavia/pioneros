from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    url(r'^inicio/$', views.home, name = 'home'),
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
    views.detail, name = 'detail'),
    url(r'^noticias/$', views.list, name = 'list'),
    url(r'^noticias/(?P<slug>[-\w]+)/$', views.category, name = 'category'),
    url(r'^patrocinadores/$', views.sponsors, name = 'sponsors'),
    url(r'^buscar/$', views.search, name = 'search'),
    url(r'^contacto/$', views.contact, name = 'contact'),
    url(r'^galeria/$', views.gallery, name = 'gallery'),
    
)