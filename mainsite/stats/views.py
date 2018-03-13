from django.http import HttpResponse
from django.shortcuts import render
from homeapp.models import PDF
from collections import Counter
from django.db.models import Count, Func, F


# Create your views here.
def index(request):
    abc=PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True)
    print(Counter(abc))
    return Counter(abc)
