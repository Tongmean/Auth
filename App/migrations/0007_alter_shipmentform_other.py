# Generated by Django 4.0.4 on 2022-08-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_shipmentform_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentform',
            name='Other',
            field=models.FileField(null=True, upload_to='OtherDocument'),
        ),
    ]