from curses.ascii import HT
from email import message
from multiprocessing import context
from tokenize import group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

#Auth
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_User, admin_only, allowed_users, user_only
from django.contrib.auth.forms import UserCreationForm
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# Create your views here.
@login_required(login_url='Loginpage')
def index(request):
    return HttpResponse("hello")
@admin_only
def SignUpuser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'The account was Created for' + username )
            
            group = Group.objects.get(name='User')
            user.groups.add(group)
            
            return HttpResponse('The account was Created')
        else:
            return HttpResponse("U from got some Problem:")
        
    return render(request, 'SignUpuser.html', {'form':form})
@admin_only
def SignUpadmin(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'The account was Created for' + username )
            
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            
            return HttpResponse('The account was Created')
        else:
            return HttpResponse("U from got some Problem:")
        
    return render(request, 'SignUpadmin.html', {'form':form})

@unauthenticated_User
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        return redirect('Home')
    return render(request, 'LoginPage.html',)

def LogOutUser(request):
    logout(request)
    return redirect('Loginpage')


@login_required(login_url='Loginpage')
def Home(request):
    return render(request,'Home.html')
@login_required(login_url='Loginpage')
def MyProfile(request):
    form = updateProfile(instance=request.user.Profile)
    if request.method == "POST":
        form = updateProfile(request.POST, request.FILES, instance=request.user.Profile)
        if form.is_valid():
            form.save()
            return redirect('Profile')
        else:
            HttpResponse('You form is not correct')
    
    return render(request, 'Profile.html',{'form':form})
#ShipmentRecord
@login_required(login_url='Loginpage')
@user_only
def ShipmentRecondList(request):
    return render(request,'ShipmentForm/ShipmentFormRecord.html')
@login_required(login_url='Loginpage')
def Home(request):
    return render(request,'Home.html')
#Action
@login_required(login_url='Loginpage')
@admin_only
def ActionRecordList(request):
    return render(request, 'Admin/Action&Cause.html')


