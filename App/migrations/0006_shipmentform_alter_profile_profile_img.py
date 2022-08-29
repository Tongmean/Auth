# Generated by Django 4.0.4 on 2022-08-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_description_profile_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentForm',
            fields=[
                ('Transaction_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Area', models.CharField(blank=True, choices=[('local', 'local'), ('Over', 'Oversea')], max_length=50, null=True)),
                ('FlightNumber', models.CharField(max_length=60, null=True)),
                ('ModeOfTranSportation', models.CharField(choices=[('Air', 'Air'), ('Truck', 'Truck'), ('Ocean', 'Ocean')], max_length=40, null=True)),
                ('Forwarder', models.CharField(max_length=50, null=True)),
                ('ShipperName', models.CharField(max_length=70, null=True)),
                ('ShipperCountry', models.CharField(max_length=70, null=True)),
                ('CustomDeclarationNumber', models.CharField(max_length=70, null=True)),
                ('InvoiceNumber', models.CharField(max_length=70, null=True)),
                ('PickTicket', models.CharField(max_length=80, null=True)),
                ('BillOfLanding', models.CharField(max_length=70, null=True)),
                ('SupplierNAme', models.CharField(max_length=70, null=True)),
                ('PartNumber', models.CharField(max_length=70, null=True)),
                ('InvoiceQuantity', models.CharField(max_length=50, null=True)),
                ('InvoiceOUM', models.CharField(max_length=70, null=True)),
                ('UnitPrice', models.CharField(max_length=50, null=True)),
                ('TotalPackage', models.CharField(max_length=50, null=True)),
                ('DateOfIncident', models.DateField(null=True)),
                ('TypeOfDiscrepancy', models.CharField(choices=[('Shortage', 'Shortage Quantity'), ('Over', 'Over Quantity'), ('Wrong', 'Wrong Parts'), ('PO', 'PO Problem')], max_length=40, null=True)),
                ('DetailOfDiscrepancy', models.CharField(max_length=70, null=True)),
                ('ShippingDocument', models.FileField(null=True, upload_to='ShippingDocument')),
                ('Other', models.FileField(blank=True, null=True, upload_to='ShippingDocument')),
                ('SubmitBy', models.CharField(max_length=70, null=True)),
                ('SubmitDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('ProcessingTime', models.CharField(max_length=70, null=True)),
                ('Status', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='Profile_Img',
            field=models.ImageField(blank=True, default='Default_User.png', null=True, upload_to='Profile_pic'),
        ),
    ]