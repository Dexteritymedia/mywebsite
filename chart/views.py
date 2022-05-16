from django.shortcuts import render

# Create your views here.
from django.db.models import Sum
from django.views.generic import TemplateView
from slick_reporting.views import SlicKReportView
from slick_reporting.fields import SlicKReportField
from .models import BitcoinChart

class index(TemplateView):
    template_name='.html'

class Total(SlicKReportView):
    report_model=BitcoinChart
    date_field='date'
    #group_by=''
    columns=['date','value']


    chart_settings = [{
        'type':'line',
        'data_source':'value',
        'title_source':['name'],
        'title':'Bitcoin In Nigeria',
    },]
