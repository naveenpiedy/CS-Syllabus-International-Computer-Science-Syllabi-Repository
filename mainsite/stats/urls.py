from django.urls import path

from . import views

app_name = 'stats'
urlpatterns = [
    path('', views.index, name='stats_page'),
    path('university',views.analyze,name='analyze'),
    path('analyze',views.uni_analysis,name='uni_analysis')
    # path('analyze',views.analyze,name='analyze'),
    # path('university',views.uni_analysis,name='uni_analysis'),
]