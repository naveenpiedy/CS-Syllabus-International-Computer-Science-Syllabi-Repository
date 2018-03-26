from django.urls import path

from . import views

app_name = 'stats'
urlpatterns = [
    path('', views.index, name='stats_page'),
    path('analyze',views.analyze,name='analyze'),
    path('university',views.uni_anal,name='uni_anal')
]