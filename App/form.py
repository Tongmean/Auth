from dataclasses import field
from django import forms
from typing_extensions import Required
import email
from email.headerregistry import Group
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from typing_extensions import Required
from urllib import request
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1', 'password2']
        
#
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = SetPasswordForm
        field = '__all__'

class updateProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['Fullname', 'Description','Profile_Img','Email' ]
        
class Shipmentrecord(ModelForm):
    AREA = (
        ('local' , 'local'),
        ('Oversea' , 'Oversea'),
    )
    Area = forms.ChoiceField(required=True, label= '', choices=AREA)
    MODEOFTRANSPORTAION = (
        ('Air' , 'Air'),
        ('Truck' , 'Truck'),
        ('Ocean' , 'Ocean') ,
    )
    ModeOfTranSportation = forms.ChoiceField(required=True, label= '', choices= MODEOFTRANSPORTAION )
    Forwarder = forms.CharField(required=True, label= '')
    ShipperCountry = forms.CharField(required=True, label= '')
    CustomDeclarationNumber= forms.CharField(required=True, label= '')
    InvoiceNumber= forms.CharField(required=True, label= '')
    PickTicket= forms.CharField(required=True, label= '')
    BillOfLanding= forms.CharField(required=True, label= '')
    PickTicket= forms.CharField(required=True, label= '')
    BillOfLanding= forms.CharField(required=True, label= '')
    SupplierNAme= forms.CharField(required=True, label= '')
    PartNumber= forms.CharField(required=True, label= '')
    InvoiceQuantity = forms.CharField(required=True, label= '')
    # InvoiceOUM = forms.CharField(required=True, label= '')
    TotalPackage= forms.CharField(required=True, label= '')
    UnitPrice= forms.CharField(required=True, label= '')
    PartDescription = forms.CharField(required=True, label= '')
    class Meta:
        model = ShipmentForm
        fields = '__all__'
        labels = {
            'Area': '',
            'FlightNumber':'',
            'ModeOfTranSportation':'',
            'Forwarder':'',
            'ShipperName':'',
            'ShipperCountry':'',
            'CustomDeclarationNumber':'',
            'InvoiceNumber':'',
            'PickTicket':'',
            'BillOfLanding':'',
            "SupplierNAme":'',
            'PartNumber':'',
            'InvoiceQuantity':'',
            'InvoiceOUM':'',
            'TypeOfDiscrepancy':'',
            'DetailOfDiscrepancy':'',
            'ShippingDocument':'',
            'Other':'',
            'TotalPackage':'',
            'UnitPrice':'',
        }
        Widgets = {
            'Area': forms.CharField(required=False),
            # 'ModeOfTranSportation':forms.CharField(required=True),
            # 'Forwarder':forms.CharField(required=True),
            # 'ShipperCountry':forms.CharField(required=True),
            # 'CustomDeclarationNumber':forms.CharField(required=True),
            # 'InvoiceNumber':forms.CharField(required=True),
            # 'PickTicket':forms.CharField(required=True),
            # 'BillOfLanding':forms.CharField(required=True),
            # "SupplierNAme":forms.CharField(required=True),
            # 'PartNumber':forms.CharField(required=True),
            # 'InvoiceQuantity':forms.CharField(required=True),
            # 'InvoiceOUM':forms.CharField(required=True),
            # 'TypeOfDiscrepancy':forms.CharField(required=True),
            # 'DetailOfDiscrepancy':forms.CharField(required=True),
            # 'ShippingDocument':forms.CharField(required=True),
            # 'Other':forms.CharField(required=True),
            # 'TotalPackage':forms.CharField(required=True),
            # 'UnitPrice':forms.CharField(required=True),
        }
        
class ChangeStatus(ModelForm):
    class Meta:
        model = ShipmentForm
        fields = ['Status']

class ActionCauseForm(ModelForm):
    class Meta:
        model = ActionCause
        fields = '__all__'
        
