from distutils.command.upload import upload
from operator import truediv
from pickle import TRUE
import profile
from re import T
from turtle import forward
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True ,related_name='Profile')
    Fullname = models.CharField(max_length=50, null=True)
    Description = models.CharField(max_length=60, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    Profile_Img = models.ImageField(null= True, blank= True, default='Default_User.png', upload_to='Profile_pic')
    
    def __str__(self):
        return self.Fullname
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null= True)
    
    def __self__(self):
        return self.name

#@receiver(post_save, sender=User)
def create_Profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance ,Fullname = instance.username)
        print('Profile Created')
        
post_save.connect(create_Profile, sender = User)


class ShipmentForm(models.Model):
    Transaction_Number = models.AutoField(primary_key = True, null=False)
    AREA = (
        ('local' , 'local'),
        ('Over' , 'Oversea'),
    )
    Area = models.CharField(max_length=50, blank= True, null= True, choices=AREA)
    FlightNumber = models.CharField(max_length=60, null= True, blank= True)
    MODEOFTRANSPORTAION = (
        ('Air' , 'Air'),
        ('Truck' , 'Truck'),
        ('Ocean' , 'Ocean') ,
    )
    ModeOfTranSportation = models.CharField(max_length=40, null = True, blank= True, choices = MODEOFTRANSPORTAION)
    Forwarder = models.CharField(max_length=50, blank= True, null =True)
    ShipperName = models.CharField(max_length=70, blank= True, null =True)
    ShipperCountry = models.CharField(max_length=70, null =True, blank= True)
    CustomDeclarationNumber = models.CharField(max_length=70, null =True, blank= True)
    InvoiceNumber = models.CharField(max_length=70, null =True, blank= True)
    PickTicket = models.CharField(max_length=80, null =True, blank= True)
    BillOfLanding = models.CharField(max_length=70, null =True, blank= True)
    SupplierNAme = models.CharField(max_length=70, null =True, blank= True)
    PartNumber = models.CharField(max_length=70, null =True, blank= True)
    InvoiceQuantity = models.CharField(max_length=50, null =True, blank= True)
    INVOICEUOM = (
        ('Each','Each'),
        ('Carton', 'Carton'),
        ('Pail', 'Pail'),
        ('Piece', 'Piece'),
        ('Pair', 'Pair'),
        ('Bottle', 'Bottle'),
    )
    InvoiceOUM = models.CharField(max_length=70, null =True, blank= True, choices=INVOICEUOM)
    UnitPrice = models.CharField(max_length=50, null =True, blank= True)
    TotalPackage = models.CharField(max_length=50, null =True, blank= True)
    DateOfIncident = models.DateField(null= True,max_length=30, blank= True)
    TYPEOFDISCREPANCY = (
        ('Shortage' , 'Shortage Quantity'),
        ('Over' , 'Over Quantity'),
        ('Wrong' , 'Wrong Parts'),
        ('PO' , 'PO Problem'),
    )
    TypeOfDiscrepancy = models.CharField(max_length=40, null= True, choices=TYPEOFDISCREPANCY, blank= True)
    DetailOfDiscrepancy = models.CharField(max_length=70, null =True, blank= True)
    ShippingDocument = models.FileField(null = True, upload_to ='ShippingDocument' , blank= True)
    Other = models.FileField(null = True, upload_to ='OtherDocument', blank= True)
    SubmitBy = models.CharField(max_length=70, null =True, blank= True)
    SubmitDate =  models.DateTimeField(auto_now_add=True, null=True, blank= True)
    ProcessingTime = models.CharField(max_length=70, null =True, blank= True)
    Status = models.CharField(max_length=25, null =True, blank= True)
        
    def __self__(self):
        return self.Area
    

class ActionCause(models.Model):
    ActionID = models.AutoField(primary_key = True, null=False)
    Transaction_Number = models.ForeignKey(ShipmentForm, on_delete=models.CASCADE, blank=True, null=True)
    RootCause = models.CharField(max_length=150, null = True, blank=True)
    ACTION =(
        ('Replace','Replace or Return Shipment'),
        ('Correct','Correct Invoice'),
        ('Credit','Credit Note')
    )
    Action = models.CharField(max_length=30, blank=True, null=True, choices=ACTION)
    ReferenceDocument = models.FileField(upload_to='ReferenceDocument', max_length=100, blank=True, null=True)
    ReportBy = models.CharField(max_length=50, null = True, blank=True)
    ReportDate = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    
    def __self__(self):
        return self.RootCause
