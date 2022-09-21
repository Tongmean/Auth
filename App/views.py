from asyncore import write
from curses.ascii import HT
from email import message
from django.contrib.sessions.models import Session
from multiprocessing import context
import re
from django.utils import timezone
from tokenize import group
from urllib import response
from xml.etree.ElementTree import PI
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .filter import *
#Auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_User, admin_only, allowed_users, user_only
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model

#Datecheat
from datetime import date , datetime
from django.utils.timezone import datetime # Create your views here.
import csv
from django.http import FileResponse
import io

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
@login_required(login_url='Loginpage')
def Genpdf(request, pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)
    records = ActionCause.objects.filter(Transaction_Number__Transaction_Number = pk )
    print(records)
    lines = [""]

    for record in records:
        lines.append("-------------------------------")
        
        
        #----
        lines.append("")
        lines.append("Discrepancy record Detail  :"  + str(record.Transaction_Number.Transaction_Number))
        lines.append("--------------------------")
        lines.append("")
        lines.append("Transaction_Number    :  "+str(record.Transaction_Number.Transaction_Number))
        lines.append("Area"+"               :  "+ str(record.Transaction_Number.Area))
        lines.append("Flight Number         :  "+str(record.Transaction_Number.FlightNumber))
        lines.append("Mode of transportation:  "+str(record.Transaction_Number.ModeOfTranSportation))
        lines.append("Forwarder             :  "+str(record.Transaction_Number.Forwarder))
        lines.append("Shipper Name          :  "+str(record.Transaction_Number.ShipperName))
        lines.append("Shipper Country       :  "+str(record.Transaction_Number.ShipperCountry))
        lines.append("Declaration Number    :  "+str(record.Transaction_Number.CustomDeclarationNumber))
        lines.append("Invoice Number        :  "+str(record.Transaction_Number.InvoiceNumber))
        lines.append("Pick Ticketor         :  "+str(record.Transaction_Number.PickTicket))
        lines.append("Bill of landing       :  "+str(record.Transaction_Number.BillOfLanding))
        lines.append("Supplier Name         :  "+str(record.Transaction_Number.SupplierNAme))
        lines.append("Part Number           :  "+str(record.Transaction_Number.PartNumber))
        lines.append("Invoice Quantity      :  "+str(record.Transaction_Number.InvoiceQuantity))
        lines.append("Invoice UOM           :  "+str(record.Transaction_Number.InvoiceOUM))
        lines.append("Unit Price            :  "+str(record.Transaction_Number.UnitPrice))
        lines.append("Total Package         :  "+str(record.Transaction_Number.TotalPackage))
        lines.append("Date of Incident      :  "+str(record.Transaction_Number.DateOfIncident))
        lines.append("Type of Discrepancy   :  "+str(record.Transaction_Number.TypeOfDiscrepancy))
        lines.append("Detail of Discrepancy :  "+str(record.Transaction_Number.DetailOfDiscrepancy))
        lines.append("Submit By             :  "+str(record.Transaction_Number.SubmitBy))
        lines.append("Submit Date           :  "+str(record.Transaction_Number.SubmitDate))
        lines.append("Status                :  "+str( record.Transaction_Number.Status))
        lines.append("-----------------------------------------    ")
        lines.append("")
        lines.append("RootCause         :  " + str(record.RootCause))
        lines.append("Action            :  " + str(record.Action))
        lines.append("Report Date       :  " + str(record.ReportDate))
        lines.append("Report By         :  " + str(record.ReportBy))
  

    
    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename = 'Discrepancy Detail ' + str(pk) + '.pdf')


@login_required(login_url='Loginpage')
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

@login_required(login_url='Loginpage')
def SignUpuser(request):
    form = CreateUserForm()
    if request.method == "POST":
        username = request.POST.get('username')
        if User.objects.filter(username = username).exists():
            messages.success(request, 'The username Already Exist :' + ' ' + username )
            # return redirect('managemanagement')
        else:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                group = Group.objects.get(name='User')
                user.groups.add(group)
                
                messages.success(request, 'The account was Created for :' + ' ' + username )
                return redirect('managemanagement')
            else:
                messages.error(request, 'Please Check again' )
                # return HttpResponse("U from got some Problem:")
        
    return render(request, 'SignUpuser.html', {'form':form})


@login_required(login_url='Loginpage')
def SignUpadmin(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            messages.success(request, 'The account was Created for' + username )
        else:
            messages.error(request, 'The account was Created for :' + ' ' + username )
        
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
            messages.info(request, 'We have '+ str(Shipform) + ' Forms to insert AddAction')
            return redirect('Home')
        else:
            messages.error(request, 'Please input correctly')
            
    
    return render(request, 'LoginPage.html')

def LogOutUser(request):
    logout(request)
    return redirect('Loginpage')

@login_required(login_url='Loginpage')
@admin_only
def managemanagement(request):
    # sessions = Session.objects.filter(expire_date__gte=datetime.now())
    # # session = request.Session
    # print(sessions)
    
    
    all_users = Profile.objects.all()
    return render(request, 'Usermanagement.html',{'all_users':all_users})


@login_required(login_url='Loginpage')
@admin_only
def resetPass(request, UserID):
    u = User.objects.get(username=UserID)
    form = SetPasswordForm(u)
    if request.method == 'POST':
        form = SetPasswordForm(user = u , data = request.POST)
        if form.is_valid():
           form.save()
           update_session_auth_hash(request, form.user)
           messages.success(request, 'Password have change successfully')
           return redirect('managemanagement')
        else:
            messages.error(request, 'Please try again')
        
    
    return redirect('managemanagement')


@login_required(login_url='Loginpage')
@admin_only
def DeleteUser(request, pk):
    Delete = User.objects.filter( id = pk)
    Delete.delete()
    print(Delete)
    messages.success(request, 'You have delete User Successfully')
    return redirect('managemanagement')


# Delete.delete()
@login_required(login_url='Loginpage')
def DiscrepancyRecord(request):
    records = ActionCause.objects.filter(Transaction_Number__Status="Close").order_by('-Transaction_Number')
    
    return render(request,'DiscrepancyList.html', {'records':records})


@login_required(login_url='Loginpage')
def MyProfile(request):
    user = request.user.Profile.Email
    print(user)
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

@login_required(login_url='Loginpage')
def Dashboard(request):
    my_date = date.today()
    my_day = datetime.now().day
    # my_week = datetime.now().week
    this_month = datetime.now().month
    this_year = datetime.now().year
    year, week_num, day_of_week = my_date.isocalendar()
    #Typeof
    Shortage = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Shortage Quantity')
    Over = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Over Quantity')
    Wrong = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Wrong Parts')
    Mixed = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'Mixed Parts')
    PO = ShipmentForm.objects.filter(Status ='Close', TypeOfDiscrepancy = 'PO Problem')
    #Dashboard Filter type
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
    #Area
    local = ShipmentForm.objects.filter(Status ='Close', Area = 'local')
    Oversea = ShipmentForm.objects.filter(Status ='Close', Area = 'Oversea')
    
    local = ShipmentFilter(request.GET, queryset= local)
    local = local.qs.count()
    
    Oversea= ShipmentFilter(request.GET, queryset= Oversea)
    Oversea = Oversea.qs.count()
 
    #Modeoftransportation
    Air = ShipmentForm.objects.filter(Status ='Close', ModeOfTranSportation = 'Air')
    Truck = ShipmentForm.objects.filter(Status ='Close', ModeOfTranSportation = 'Truck')
    Ocean = ShipmentForm.objects.filter(Status ='Close', ModeOfTranSportation = 'Ocean')
    Air = ShipmentFilter(request.GET, queryset= Air)
    Air = Air.qs.count()
    Truck = ShipmentFilter(request.GET, queryset= Truck)
    Truck = Truck.qs.count()
    Ocean = ShipmentFilter(request.GET, queryset= Ocean)
    Ocean = Ocean.qs.count()
    
    Monly=[]
    
    for i in range(1,13):
        mon = ActionCause.objects.filter(ReportDate__month = i , ReportDate__year =  this_year,).count()
        Monly.append(mon)
    
    weekly =[]
    for i in range(1,8):
        week = ActionCause.objects.filter(ReportDate__week_day= i ,ReportDate__week = week_num  ,ReportDate__month = this_month , ReportDate__year =  this_year,).count()
        weekly.append(week)
    
    print(weekly)
    record = ShipmentForm.objects.filter(Status= 'Close')
    records = record.select_related()
    maxweek = ActionCause.objects.filter(ReportDate__week = week_num  ,ReportDate__month = this_month , ReportDate__year =  this_year,).count() + 5
    # print(records)
    myFilter = ShipmentFilter(request.GET, queryset= records)
    records = myFilter.qs       
    context = {'records':records, 'myFilter':myFilter,
               'Shortage':Shortage, 'Over':Over
               , 'Wrong':Wrong, 'Mixed':Mixed, 'PO':PO, 
               'Oversea':Oversea, 'local':local,
               'Air':Air, 'Truck':Truck, 'Ocean':Ocean,
               'Monly':Monly, 'weekly':weekly,'maxweek':maxweek
               
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
    useremail = request.user.Profile.Email
    if 'submit' in request.POST: 
        form = Shipmentrecord(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.Status= 'Submitted'
            f.SubmitBy = useremail
            f.save()
            messages.success(request, 'Your form was Submit successfully')
            return redirect('MyActivities')
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
            return redirect('MyActivities')
        else:
            messages.warning(request, 'Please correct your form')
    return render(request, 'ShipmentForm/InsertRecord.html',{'form':form})

@login_required(login_url='Loginpage')
@user_only
def MyActivities(request):
    useremail = request.user.Profile.Email
    record = ShipmentForm.objects.filter(SubmitBy = useremail ).order_by("-Transaction_Number")
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
    
    Today = ActionCause.objects.filter(ReportDate__day = my_day, ReportDate__month = this_month ,ReportDate__year = this_year ).count()
    week = ActionCause.objects.filter(ReportDate__week = week_num, ReportDate__month = this_month, ReportDate__year = this_year ).count()
    month = ActionCause.objects.filter(ReportDate__month = this_month,ReportDate__year = this_year ).count()
    year = ActionCause.objects.filter(ReportDate__year = this_year ).count()
    
   
    #Weekly 
    Mon = ActionCause.objects.filter(ReportDate__week_day = 2, ReportDate__week =  week_num).count()
    Tues = ActionCause.objects.filter(ReportDate__week_day = 3, ReportDate__week =  week_num).count()
    Wen = ActionCause.objects.filter(ReportDate__week_day = 4, ReportDate__week =  week_num).count()
    Thur = ActionCause.objects.filter(ReportDate__week_day = 5, ReportDate__week =  week_num).count()
    Fri = ActionCause.objects.filter(ReportDate__week_day = 6, ReportDate__week =  week_num).count()
    Sat = ActionCause.objects.filter(ReportDate__week_day = 7, ReportDate__week =  week_num).count()
    Sun = ActionCause.objects.filter(ReportDate__week_day = 1, ReportDate__week =  week_num).count()
    #Weeklymodeoftransportation
    MonAri = ActionCause.objects.filter(ReportDate__week_day = 2, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    TuesAri = ActionCause.objects.filter(ReportDate__week_day = 3, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    WenAri = ActionCause.objects.filter(ReportDate__week_day = 4, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    ThurAri = ActionCause.objects.filter(ReportDate__week_day = 5, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    FriAri = ActionCause.objects.filter(ReportDate__week_day = 6, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    SatAri = ActionCause.objects.filter(ReportDate__week_day = 7, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    SunAri = ActionCause.objects.filter(ReportDate__week_day = 1, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Air').count()
    
    MonTruck = ActionCause.objects.filter(ReportDate__week_day = 2, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    TuesTruck = ActionCause.objects.filter(ReportDate__week_day = 3, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    WenTruck = ActionCause.objects.filter(ReportDate__week_day = 4, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    ThurTruck = ActionCause.objects.filter(ReportDate__week_day = 5, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    FriTruck = ActionCause.objects.filter(ReportDate__week_day = 6, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    SatTruck = ActionCause.objects.filter(ReportDate__week_day = 7, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    SunTruck = ActionCause.objects.filter(ReportDate__week_day = 1, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Truck').count()
    
    MonOcean = ActionCause.objects.filter(ReportDate__week_day = 2, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    TuesOcean = ActionCause.objects.filter(ReportDate__week_day = 3, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    WenOcean = ActionCause.objects.filter(ReportDate__week_day = 4, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    ThurOcean = ActionCause.objects.filter(ReportDate__week_day = 5, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    FriOcean = ActionCause.objects.filter(ReportDate__week_day = 6, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    SatOcean = ActionCause.objects.filter(ReportDate__week_day = 7, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    SunOcean = ActionCause.objects.filter(ReportDate__week_day = 1, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count()
    #List
    # Month = []
    # for x in range(1,8):
    #     Month.append(ActionCause.objects.filter(ReportDate__week_day = x, ReportDate__week =  week_num, Transaction_Number__ModeOfTranSportation = 'Ocean').count())
    print(timezone.now())
    print(request.user.email + request.user.Profile.Email)
    Shipform = ShipmentForm.objects.filter(Status= 'Submitted').count()

   
    context = {'record':record, 'Shortage':Shortage, 'Over':Over
               , 'Wrong':Wrong, 'Mixed':Mixed, 'PO':PO, 'Today':Today, 
               'month':month, 'year':year, 'week':week,
               'Mon':Mon, 'Tues':Tues, 'Wen':Wen, 'Thur':Thur, 'Fri':Fri, 'Sat':Sat, 'Sun':Sun,
               'MonAri':MonAri, 'TuesAri':TuesAri, 'WenAri':WenAri, 'ThurAri':ThurAri, 'FriAri':FriAri, 'SatAri':SatAri, 'SunAri':SunAri,
               'MonTruck':MonTruck, 'TuesTruck':TuesTruck, 'WenTruck':WenTruck, 'ThurTruck':ThurTruck, 'FriTruck':FriTruck, 'SatTruck':SatTruck, 'SunTruck':SunTruck,
               'MonOcean':MonOcean, 'TuesOcean':TuesOcean, 'WenOcean':WenOcean, 'ThurOcean':ThurOcean, 'FriOcean':FriOcean, 'SatOcean':SatOcean, 'SunOcean':SunOcean,
               'Shipform':Shipform
               }
    return render(request,'Home.html', context)


@login_required(login_url='Loginpage')
def Update(request, pk):
    Update = ShipmentForm.objects.get( Transaction_Number = pk)
    form = Shipmentrecord( instance=Update )
    # if request.method == 'POST':
    #     useremail = request.user.email
    #     form = Shipmentrecord(request.POST, request.FILES, instance=Update)
    #     if form.is_valid():
    #         f= form.save(commit=False)
    #         f.SubmitBy = useremail
    #         f.Status= 'Submitted'
    #         f.save()
    #         messages.success(request, 'You have update Successfully')
    #         return redirect('MyActivities')
    #     else:
    #         messages.warning(request, 'You have got some errors')
            
    useremail = request.user.Profile.Email        
    if 'submit' in request.POST: 
        form = Shipmentrecord(request.POST, request.FILES, instance=Update)
        if form.is_valid():
            f = form.save(commit=False)
            f.Status= 'Submitted'
            f.SubmitBy = useremail
            f.save()
            messages.success(request, 'Your form was Submit successfully')
            return redirect('MyActivities')
        else:
            return HttpResponse('UR form get some Error')
            messages.warning(request, 'Please correct Your form')
    if 'save' in request.POST: 
        form = Shipmentrecord(request.POST, request.FILES, instance=Update)
        if form.is_valid():
            f = form.save(commit=False)
            f.Status= 'Saved'
            f.SubmitBy = useremail
            f.save()
            messages.success(request, 'Your form was Save successfully')
            return redirect('MyActivities')
        else:
            messages.warning(request, 'Please correct your form')
    return render(request,'ShipmentForm/Update.html',{'form':form})

def Delete(request, pk):
    Delete = ShipmentForm.objects.get(Transaction_Number = pk)
    form = ChangeStatus( instance=Delete )
    if request.method == 'POST':
        form = ChangeStatus(request.POST, request.FILES, instance = Delete)
        if form.is_valid:
            f = form.save(commit=False)
            f.Status = 'Cancelled'
            f.save()
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
        useremail = request.user.Profile.Email
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
    
    useremail = request.user.Profile.Email
    
    record = ActionCause.objects.filter(ReportBy = useremail)
    
    return render(request, 'Admin/MyTask.html',{'records':record})



# @login_required(login_url='Loginpage')
def HomePage(request):
    record = ActionCause.objects.all().count()
    return render(request,'HomePage.html')