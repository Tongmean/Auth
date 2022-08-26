# Generated by Django 4.0.4 on 2022-08-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_profile_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Full_Name',
            new_name='name',
        ),
    ]