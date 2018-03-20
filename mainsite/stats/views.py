from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from homeapp.models import PDF
from homeapp.models import Tag
from collections import Counter
from django.db.models import Count, Func, F
from mainsite import settings
import random
from jchart.config import rgba, Axes, Legend, Tick
import json
from jchart import Chart


# Create your views here.


class PieChart(Chart):
    chart_type = 'doughnut'
    legend = {'position': 'bottom'}

    def geting_local_data(self, labels, data):
        self.local_data = data
        self.local_labels = labels

    def get_labels(self, *args, **kwargs):
        return self.local_labels

    def get_datasets(self, *args, **kwargs):
        colors = []

        for _ in self.local_data:
            red = random.randint(0, 256)
            green = random.randint(0, 256)
            blue = random.randint(0, 256)
            colors.append(rgba(red, green, blue, 0.3))

        return [{
            'label': "My Dataset",
            'data': self.local_data,
            'backgroundColor': colors
        }]

def returnk(**kwargs):
    return dict(**kwargs)

class BarChart(Chart):
    chart_type = 'bar'
    tick = {"beginAtZero":'true'}
    f = returnk(beginAtZero=True)
    print(f)
    scales = {
        'yAxes': [{'ticks': returnk(beginAtZero='true')}],
    }

    def geting_local_data(self, labels, data):
        self.local_data = data
        self.local_labels = labels

    def get_labels(self, *args, **kwargs):
        return self.local_labels

    def get_datasets(self, *args, **kwargs):
        colors = []

        for _ in self.local_data:
            red = random.randint(0, 256)
            green = random.randint(0, 256)
            blue = random.randint(0, 256)
            colors.append(rgba(red, green, blue, 0.3))

        return [{
            'label': "My Dataset",
            'data': self.local_data,
            'backgroundColor': colors
        }]


def index(request):
    c = {}
    c.update(csrf(request))
    abc = PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).annotate(
        num=Count('list'))

    list_tags = list(abc)
    list_dic = {}
    for i in range(0, len(list_tags), 2):
        list_dic[list_tags[i]] = list_tags[i + 1]

    pie = PieChart()
    bar = BarChart()
    if len(list_dic) > 20:
        sorted_dic = sorted(list_dic.items(), key=lambda x: x[1])[:15]
        sorted_values, sorted_data = zip(*sorted_dic)
        print(sorted_values, sorted_data)
        pie.geting_local_data(list(sorted_values), list(sorted_data))
        bar.geting_local_data(list(sorted_values), list(sorted_data))
    else:
        pie.geting_local_data(list(list_dic.keys()), list(list_dic.values()))
        bar.geting_local_data(list(list_dic.keys()), list(list_dic.values()))
    # print(list_dic)
    return render(request, 'stats/overall.html', {'piechart': pie, 'barchart':bar}, c)

def analyze(request):
    c = {}
    c.update(csrf(request))
    print(request.POST)
    search_lev=''
    if request.POST['year'] == 'Freshman':
        search_lev = 'Freshman'
    if request.POST['year'] == 'Junior':
        search_lev = 'Junior'
    if request.POST['year'] == 'Masters':
        search_lev = 'Masters'
    if request.POST['year'] == 'Doctorate':
        search_lev = 'Doctorate'
    if request.POST['year'] == 'Senior':
        search_lev = 'Senior'
    if request.POST['year'] == 'Sophomore':
        search_lev = 'Sophomore'
    if request.POST['year'] == 'None':
        search_lev= 'None'
    search_uni=request.POST['University']

    if search_uni=='' and search_lev=='None':
        abc = PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).annotate(num=Count('list'))
    elif search_uni=='' and search_lev!='None':
        abc = PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).filter(
            year=search_lev).annotate(num=Count('list'))
    elif search_uni!='' and search_lev=='None':
        abc = PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).filter(
            university=search_uni).annotate(num=Count('list'))
    else:
        abc = PDF.objects.annotate(list=Func(F('pdf_tags'), function='unnest')).values_list('list', flat=True).filter(
            university=search_uni,year=search_lev).annotate(num=Count('list'))
    list_tags = list(abc)
    list_dic = {}
    for i in range(0, len(list_tags), 2):
        list_dic[list_tags[i]] = list_tags[i + 1]
    print(list_dic)



    return render(request,'stats/universityStats.html',c)