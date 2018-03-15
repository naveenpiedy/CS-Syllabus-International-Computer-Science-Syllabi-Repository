from django.http import HttpResponse
from django.shortcuts import render
from homeapp.models import PDF
from chartjs_engine.views.engine import ChartEngine
from collections import Counter
from django.db.models import Count, Func, F
from mainsite import settings
import json


# Create your views here.
def index(request):
    abc = PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).annotate(num=Count('list'))
    list_tags=list(abc)
    list_dic = {}
    for i in range(0, len(list_tags), 2):
        list_dic[list_tags[i]] = list_tags[i+1]
    # print(list_dic)
    print(json.dumps(list(list_dic.values())))
    chart_setup = {
        'chart_name': 'syllabi',
        'chart_type': 'pie',
        'chart_labels': list(list_dic.keys()) ,
        'options': 'options',
        'datasets': {
            'data1': list(list_dic.values()),
            #'data1': [1,2,3,4,5]
        }
    }
    engine = ChartEngine(**chart_setup)
    chart = engine.make_chart()
    return HttpResponse(settings.CHARTJS_SCRIPT + chart)
