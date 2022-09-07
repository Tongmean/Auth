from dataclasses import field
import email
from email.headerregistry import Group
from pyexpat import model
from socket import fromshare
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
        fields = ['Fullname', 'Description','Profile_Img' ]
        
class Shipmentrecord(ModelForm):
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
        
class ChangeStatus(ModelForm):
    class Meta:
        model = ShipmentForm
        fields = ['Status']

class ActionCauseForm(ModelForm):
    class Meta:
        model = ActionCause
        fields = '__all__'
        
