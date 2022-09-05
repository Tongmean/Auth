from asyncore import write
from curses.ascii import HT
from email import message
from multiprocessing import context
import re
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
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_User, admin_only, allowed_users, user_only
from django.contrib.auth.forms import UserCreationForm
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
@admin_only
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
                messages.ERROR(request, 'The account was Created for :' + ' ' + username )
                # return HttpResponse("U from got some Problem:")
        
    return render(request, 'SignUpuser.html', {'form':form})


@admin_only
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
            messages.ERROR(request, 'The account was Created for :' + ' ' + username )
        
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

@login_required(login_url='Loginpage')
@admin_only
def managemanagement(request):

    all_users = Profile.objects.all()
    return render(request, 'Usermanagement.html',{'all_users':all_users})

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
    #Invoice
    Each = ShipmentForm.objects.filter(Status ='Close', InvoiceOUM = 'Each')
    Carton = ShipmentForm.objects.filter(Status ='Close', InvoiceOUM = 'Carton')
    Pail = ShipmentForm.objects.filter(Status ='Close', InvoiceOUM = 'Pail')
    Piece = ShipmentForm.objects.filter(Status ='Close', InvoiceOUM = 'Piece')
    Pair = ShipmentForm.objects.filter(Status ='Close', InvoiceOUM = 'Pair')
    Bottle = ShipmentForm.objects.filter(Status ='Close', InvoiceOUM = 'Bottle')
    
    Each = ShipmentFilter(request.GET, queryset= Each)
    Each = Each.qs.count()
    
    Carton = ShipmentFilter(request.GET, queryset= Carton)
    Carton = Carton.qs.count()
    
    Pail = ShipmentFilter(request.GET, queryset= Pail)
    Pail = Pail.qs.count()
    
    Piece = ShipmentFilter(request.GET, queryset= Piece)
    Piece = Piece.qs.count()
    
    Pair = ShipmentFilter(request.GET, queryset= Pair)
    Pair = Pair.qs.count()
    
    Bottle = ShipmentFilter(request.GET, queryset= Bottle)
    Bottle = Bottle.qs.count()
    
    
    
    records = ShipmentForm.objects.filter(Status= 'Close').values()
    myFilter = ShipmentFilter(request.GET, queryset= records)
    records = myFilter.qs       
    context = {'records':records, 'myFilter':myFilter,
               'Shortage':Shortage, 'Over':Over
               , 'Wrong':Wrong, 'Mixed':Mixed, 'PO':PO, 
               'Oversea':Oversea, 'local':local,
               'Each':Each, 'Carton':Carton, 'Pail':Pail,
               'Piece':Piece, 'Pair':Pair, 'Bottle':Bottle
               
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
    record = ShipmentForm.objects.filter(SubmitBy = useremail ).order_by("-Transaction_Number").values
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



@login_required(login_url='Loginpage')
def HomePage(request):
    record = ActionCause.objects.all().count()
    return render(request,'HomePage.html')