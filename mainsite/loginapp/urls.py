from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('forget_step1', views.forget_password_step1,name='forget_password_step1'),
    url(r'^$', views.index, name='index'),
]