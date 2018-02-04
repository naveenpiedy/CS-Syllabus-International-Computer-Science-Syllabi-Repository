from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('search/title=<str:pdfname>', views.Acc_Pdf.as_view(), name='search_list'),
]