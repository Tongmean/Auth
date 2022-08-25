from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
#Auth
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_User, admin_only, allowed_users
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# Create your views here.
def index(request):
    return HttpResponse("hello")
@unauthenticated_User
def SignUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Loginpage')
        else:
            return HttpResponse("U from got some Problem:")
        
    return render(request, 'SignUp.html', {'form':form})
@unauthenticated_User
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
    return render(request, 'LoginPage.html',)

def LogOutUser(request):
    logout(request)
    return redirect('Loginpage')


@login_required(login_url='Loginpage')
def Home(request):
    return render(request,'Home.html')

def Profile(request):
    Profile = Profile.objects.a()
    print(Profile)
    return render(request, 'Profile.html')
#ShipmentRecord
@login_required(login_url='Loginpage')
def ShipmentRecondList(request):
    return render(request,'ShipmentForm/ShipmentFormRecord.html')
@login_required(login_url='Loginpage')
def HomeShipment(request):
    return render(request,'ShipmentForm/Home.html')
#Action
def ActionRecordList(request):
    return render(request, 'Admin/Action&Cause.html')


