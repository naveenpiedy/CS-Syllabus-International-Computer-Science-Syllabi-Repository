import mimetypes
import os
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from homeapp.models import PDF
import requests
from .serializers import SearchSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from mainsite import settings
# Create your views here.
from rest_framework import generics


class Acc_Pdf(generics.ListCreateAPIView):
    queryset = PDF.objects.all()
    serializer_class = SearchSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('pdfName', 'professor_name', 'subjectName', 'pdf_desc', 'pdf_topic', 'uploaders', 'university','id')
    search_fields = ['pdfName', 'professor_name', 'subjectName', 'uploaders', 'university', 'pdf_tags',]

    def get_queryset(self):
        pdf_tag = self.request.GET.getlist('pdf_tags')
        if not pdf_tag:
            # I forget to give the ISSUE NUMBER!
            pass
        return PDF.objects.filter(pdf_tags__contains= pdf_tag)

def downloadfile(request, filename):
    with open(os.path.join(settings.MEDIA_ROOT, filename), 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename='+filename
        return response