from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'signupapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('activate/uidb64=<str:uidb64>/token=<str:token>', views.activate, name='activate')
]