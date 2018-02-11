from django.shortcuts import render
from homeapp.models import PDF
import requests
from .serializers import SearchSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
from rest_framework import generics


class Acc_Pdf(generics.ListCreateAPIView):
    queryset = PDF.objects.all()
    serializer_class = SearchSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('user', 'pdfName', 'professor_name', 'subjectName', 'pdf_title', 'pdf_desc', 'uploader_name', 'university')
    search_fields = ['subjectName',]

    def get_queryset(self):
        pdf_tag = self.request.GET.getlist('pdf_tags')
        if not pdf_tag:
            # I forget to give the ISSUE NUMBER!
            pass
        return PDF.objects.filter(pdf_tags__contains= pdf_tag)
