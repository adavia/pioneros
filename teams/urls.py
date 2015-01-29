from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^centros/$', views.centers, name = 'centers'),
    url(r'^historia/$', views.history, name = 'history'),
    url(r'^estadio/$', views.stadium, name = 'stadium'),
    url(r'^directiva/$', views.directive, name = 'directive'),
    url(r'^plantel/$', views.team, name = 'team'),
    url(r'^cuerpo_tecnico/$', views.coach, name = 'coach'),
    url(r'^posiciones/$', views.positions, name = 'positions'),
    url(r'^aficion/$', views.games, name = 'games'),
    #url(r'^noticias/buscar/$', views.article_search_view, name = 'article_search_view'),
    #url(r'^noticias/$', views.article_list_view, name = 'article_list_view'),
    #url(r'^noticias/(?P<slug>[-\w]+)/$', views.article_category_view, name = 'article_category_view'),
    #url(r'^seccion/(?P<slug>[-\w]+)/$', views.article_section_view, name = 'article_section_view'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
    #views.article_detail_view, name = 'article_detail_view'),
    #url(r'^video/(?P<slug>[-\w]+)/$', views.video_detail_view, name = 'video_detail_view'),
)