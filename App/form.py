from dataclasses import field
import email
from email.headerregistry import Group
from socket import fromshare
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
#
class updateProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['Fullname', 'Description','Profile_Img' ]