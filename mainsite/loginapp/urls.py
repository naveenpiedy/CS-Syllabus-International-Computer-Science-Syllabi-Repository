from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'loginapp'
urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    path('forget_step1', views.forget_password_step1,name='forget_password_step1'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.reset, name='reset'),
    path('reset/uidb64=<str:uidb64>/token=<str:token>', views.reset, name='reset'),
    url(r'^$', views.index, name='index')
]