# Generated by Django 4.0.4 on 2022-09-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_shipmentform_partdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shipmentform',
            name='Running_num',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
