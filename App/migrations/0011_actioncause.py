# Generated by Django 4.0.4 on 2022-08-29 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_alter_shipmentform_flightnumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCause',
            fields=[
                ('ActionID', models.AutoField(primary_key=True, serialize=False)),
                ('RootCause', models.CharField(blank=True, max_length=150, null=True)),
                ('Action', models.CharField(blank=True, choices=[('Replace', 'Replace or Return Shipment'), ('Correct', 'Correct Invoice'), ('Credit', 'Credit Note')], max_length=30, null=True)),
                ('ReferenceDocument', models.FileField(blank=True, null=True, upload_to='ReferenceDocument')),
                ('ReportBy', models.CharField(blank=True, max_length=50, null=True)),
                ('ReportDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('Transaction_Number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.shipmentform')),
            ],
        ),
    ]