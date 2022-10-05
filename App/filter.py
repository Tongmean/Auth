from cProfile import label
from cgitb import lookup
from dataclasses import field
from logging import PlaceHolder
from xml.dom.minidom import Attr
import django_filters
from django import forms
from .models import *
class ShipmentFilter(django_filters.FilterSet):
    Start_Date = django_filters.DateFilter(field_name="SubmitDate", lookup_expr ='gte', label=('Start date'), widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    End_Date = django_filters.DateFilter(field_name="SubmitDate", lookup_expr ='lte', label=('End date'), widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:
        model = ShipmentForm
        fields = ['Area','Forwarder']
        # label = {
        #     'InvoiceOUM':'InvoiceUOM',
        # }
        
# class ShipmentChartFilter(django_filters.FilterSet):
#     Start_Date = django_filters.DateFilter(field_name="SubmitDate", lookup_expr ='gte', label=('Start date'))
#     End_Date = django_filters.DateFilter(field_name="SubmitDate", lookup_expr ='lte', label=('End date'))
#     class Meta:
#         model = ShipmentForm
#         fields = ['SubmitDate']
