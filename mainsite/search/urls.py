from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('searching', TemplateView.as_view(template_name="index.html")),
    url(r'\S*', views.Acc_Pdf.as_view()),
]