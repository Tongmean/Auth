# Generated by Django 4.0.4 on 2022-08-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_shipmentform_billoflanding_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentform',
            name='FlightNumber',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='shipmentform',
            name='Other',
            field=models.FileField(blank=True, null=True, upload_to='OtherDocument'),
        ),
    ]
