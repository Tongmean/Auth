from asyncore import write
from curses.ascii import HT
from email import message
from multiprocessing import context
import re
from tokenize import group
from urllib import response
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .filter import *
#Auth
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_User, admin_only, allowed_users, user_only
from django.contrib.auth.forms import UserCreationForm
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model

#Date
from datetime import date , datetime
from django.utils.timezone import datetime # Create your views here.
import csv
def GenCSV(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = Discrepancy-List.csv'
    
    writer = csv.writer(response)
    
    records = ActionCause.objects.all()
    
    writer.writerow(['Transaction Number', 'Area', 'Flight Number','Mode Of TranSportation', 'Forwarder'  
                    ,'Shipper Name', 'Shipper Country' , 'Custom Declaration Number', 'Invoice Number'
                    ,'Pick Ticket', 'Bill Of Landing', 'Supplier Name', 'Part Number','Invoice Quantity'
                    , 'Invoice UOM', 'Unit Price', 'Total Package', 'Date Of Incident','Type Of Discrepancy'
                    , 'Detail Of Discrepancy', 'Submit By', 'Submit Date', 'Processing Time','Status'
                    , 'Root Cause', 'Action', 'Report By','Report Date'
                    ])
    
    for record in records:
        writer.writerow([record.Transaction_Number.Transaction_Number, record.Transaction_Number.Area, record.Transaction_Number.FlightNumber,
        record.Transaction_Number.ModeOfTranSportation,
        record.Transaction_Number.Forwarder,
        record.Transaction_Number.ShipperName,
        record.Transaction_Number.ShipperCountry,
        record.Transaction_Number.CustomDeclarationNumber,
        record.Transaction_Number.InvoiceNumber,
        record.Transaction_Number.PickTicket,
        record.Transaction_Number.BillOfLanding,
        record.Transaction_Number.SupplierNAme,
        record.Transaction_Number.PartNumber,
        record.Transaction_Number.InvoiceQuantity,
        record.Transaction_Number.InvoiceOUM,
        record.Transaction_Number.UnitPrice,
        record.Transaction_Number.TotalPackage,
        record.Transaction_Number.DateOfIncident,
        record.Transaction_Number.TypeOfDiscrepancy,
        record.Transaction_Number.DetailOfDiscrepancy,
        record.Transaction_Number.SubmitBy,
        record.Transaction_Number.SubmitDate,
        record.Transaction_Number.ProcessingTime,
        record.Transaction_Number.Status,
        record.RootCause,
        record.Action,
        record.ReportBy,
        record.ReportDate,
                            
                         
                         
    ])
    
    return response

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
    Shipform = ShipmentForm.objects.filter(Status= 'Submitted').count()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            
        messages.success(request, 'We have '+ str(Shipform) + ' Forms to insert AddAction')
        return redirect('Home')
    return render(request, 'LoginPage.html',)

def LogOutUser(request):
    logout(request)
    return redirect('Loginpage')

def managemanagement(request):

    all_users = Profile.objects.all()
    return render(request, 'Usermanagement.html',{'all_users':all_users})

@login_required(login_url='Loginpage')
def DiscrepancyRecord(request):
    records = ActionCause.objects.all()
    
    return render(request,'DiscrepancyList.html', {'records':records})


@login_required(login_url='Loginpage')
def MyProfile(request):
    form = updateProfile(instance=request.user.Profile)
    if request.method == "POST":
        form = updateProfile(request.POST, request.FILES, instance=request.user.Profile)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'You have Update Profile Successfully')
            return redirect('Profile')
        else:
            HttpResponse('You form is not correct')
    
    return render(request, 'Profile.html',{'form':form})

def Dashboard(request):
    Shortage = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Shortage Quantity')
    Over = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Over Quantity')
    Wrong = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Wrong Parts')
    Mixed = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Mixed Parts')
    PO = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'PO Problem')
    
    records = ShipmentForm.objects.filter(Status= 'Close').values()
    myFilter = ShipmentFilter(request.GET, queryset= records)
    records = myFilter.qs
    #Dashboard Filter
    Shortage = ShipmentFilter(request.GET, queryset= Shortage)
    Shortage = Shortage.qs.count()
    
    Over = ShipmentFilter(request.GET, queryset= Over)
    Over = Over.qs.count()
    
    Wrong = ShipmentFilter(request.GET, queryset= Wrong)
    Wrong = Wrong.qs.count()
    
    Mixed = ShipmentFilter(request.GET, queryset= Mixed)
    Mixed = Mixed.qs.count()
    
    PO = ShipmentFilter(request.GET, queryset= PO)
    PO = PO.qs.count()
       
    context = {'records':records, 'myFilter':myFilter,
               'Shortage':Shortage, 'Over':Over
               , 'Wrong':Wrong, 'Mixed':Mixed, 'PO':PO, 
    }
    return render(request,'Dashboard.html', context)

#ShipmentRecord
@login_required(login_url='Loginpage')
@user_only
def ShipmentRecondList(request):
    record = ShipmentForm.objects.all()
    
    

    return render(request,'ShipmentForm/ShipmentFormRecord.html', {'records':record})

@login_required(login_url='Loginpage')
@user_only
def InsertRecord(request):
    form = Shipmentrecord
    useremail = request.user.email
    if 'submit' in request.POST: 
        form = Shipmentrecord(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.Status= 'Submitted'
            f.SubmitBy = useremail
            f.save()
            messages.success(request, 'Your form was Submit successfully')
            return redirect('ShipmentRecordList')
        else:
            return HttpResponse('UR form get some Error')
            messages.warning(request, 'Please correct Your form')
    if 'save' in request.POST: 
        form = Shipmentrecord(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.Status= 'Saved'
            f.SubmitBy = useremail
            f.save()
            messages.success(request, 'Your form was Save successfully')
            return redirect('ShipmentRecordList')
        else:
            messages.warning(request, 'Please correct your form')
    return render(request, 'ShipmentForm/InsertRecord.html',{'form':form})

@login_required(login_url='Loginpage')
@user_only
def MyActivities(request):
    useremail = request.user.email
    record = ShipmentForm.objects.filter(SubmitBy = useremail )
    return render(request, 'ShipmentForm/MyActivities.html', {'records':record})

@login_required(login_url='Loginpage')
def Home(request):
    record = ActionCause.objects.all().count()
    Shortage = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Shortage Quantity').count()
    Over = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Over Quantity').count()
    Wrong = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Wrong Parts').count()
    Mixed = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Mixed Parts').count()
    PO = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'PO Problem').count()
    
    my_date = date.today()
    my_day = datetime.now().day
    # my_week = datetime.now().week
    this_month = datetime.now().month
    this_year = datetime.now().year
    year, week_num, day_of_week = my_date.isocalendar()
    
    Today = ActionCause.objects.filter(ReportDate__day = my_day ).count()
    week = ActionCause.objects.filter(ReportDate__week = week_num ).count()
    month = ActionCause.objects.filter(ReportDate__month = this_month ).count()
    year = ActionCause.objects.filter(ReportDate__year = this_year ).count()
    
    context = {'record':record, 'Shortage':Shortage, 'Over':Over
               , 'Wrong':Wrong, 'Mixed':Mixed, 'PO':PO, 'Today':Today, 
               'month':month, 'year':year, 'week':week }
    return render(request,'Home.html', context)

                        # datetime_published__year='2008', 
                        #  datetime_published__month='03', 
                        #  datetime_published__day='27')
                        #'all':all
@login_required(login_url='Loginpage')
def Update(request, pk):
    Update = ShipmentForm.objects.get( Transaction_Number = pk)
    form = Shipmentrecord( instance=Update )
    if request.method == 'POST':
        useremail = request.user.email
        form = Shipmentrecord(request.POST, request.FILES, instance=Update)
        if form.is_valid():
            f= form.save(commit=False)
            f.SubmitBy = useremail
            f.Status= 'Submitted'
            f.save()
            messages.success(request, 'You have update Successfully')
            return redirect('MyActivities')
        else:
            messages.warning(request, 'You have got some errors')
    return render(request,'ShipmentForm/Update.html',{'form':form})

def Delete(request, pk):
    Delete = ShipmentForm.objects.get(Transaction_Number = pk)
    Delete.delete()
    messages.success(request, 'You have record has delete Successfully')
    return redirect(MyActivities)


#Action
@login_required(login_url='Loginpage')
def ShipmentList(request):
    record = ShipmentForm.objects.filter(Status = 'Submitted')
    form1 = ActionCauseForm()
    return render(request, 'Admin/ShipmentList.html', {'records':record, 'form1':form1})


@login_required(login_url='Loginpage')
def AddAction(request, pk):
    Update = ShipmentForm.objects.get( Transaction_Number = pk)
    form = ChangeStatus( instance=Update )
    form1 = ActionCauseForm()
    if request.method == 'POST':
        useremail = request.user.email
        form1 = ActionCauseForm(request.POST, request.FILES)
        form = ChangeStatus(request.POST, request.FILES, instance = Update)
        if form1.is_valid and form.is_valid:
            f = form.save(commit=False)
            f.Status = 'Close'
            f.save()
            H = form1.save(commit=False)
            H.ReportBy = useremail
            H.save()
            messages.success(request, 'You have record has Insert Action information Successfully')
            return redirect('ShipmentList')
        else:
            HttpResponse('You have got some error')
        
    return redirect('ShipmentList')

@login_required(login_url='Loginpage')
@admin_only
def ActionRecordList(request):
    record = ActionCause.objects.all()
    return render(request, 'Admin/Action&Cause.html',{'records':record})

@login_required(login_url='Loginpage')
def MyTask(request):
    useremail = request.user.email
    record = ActionCause.objects.filter(ReportBy = useremail)

    return render(request, 'Admin/MyTask.html',{'records':record})




def HomePage(request):
    record = ActionCause.objects.all().count()
    return render(request,'HomePage.html')