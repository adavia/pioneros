from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
    url(r'^perfil/$', views.profile, name = 'edit'),
)