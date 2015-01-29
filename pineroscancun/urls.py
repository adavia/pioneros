from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
	url(r'^', include('users.urls', namespace = "user")),
   	url(r'^', include('profiles.urls', namespace = "profile")),
    url(r'^', include('articles.urls', namespace = "article")),
    url(r'^', include('teams.urls', namespace = "team")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)
