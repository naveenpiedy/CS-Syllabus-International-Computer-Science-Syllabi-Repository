from django.http import HttpResponse
from django.shortcuts import render
from homeapp.models import PDF
from collections import Counter
from django.db.models import Count, Func, F


# Create your views here.
def index(request):
    abc=PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).annotate(num=Count('list'))
    list_tags=list(abc)
    list_dic = {}
    for i in range(0, len(list_tags), 2):
        list_dic[list_tags[i]] = list_tags[i+1]
    print(list_dic)
    return list_dic
