from pickle import TRUE
import profile
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