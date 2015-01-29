from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^registro/$', views.user_signup, name='signup'),
    url(r'^ingresar/$', views.user_login, name='login'),
    url(r'^salir/$', views.user_logout, name='logout'),
    url(r'^verificacion/$', views.user_verification, name='user_verification'),
    url(r'^verificacion/(?P<uid>[^/]+)/(?P<token>[^/]+)/$', views.user_verify, name='user_verify'),
    url(r'^password-reset/$', views.user_password_reset, name='password_reset'),
    url(r'^password-reset/envio/$', views.user_password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirmacion/(?P<uidb64>.+)/(?P<token>.+)/$', 
        views.user_password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/completo/$', views.user_password_reset_complete, name='password_reset_complete'),
)