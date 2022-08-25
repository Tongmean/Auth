from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    Full_Name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=60, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    Profile_Img = models.ImageField(null= True, blank= True, default='Default-Pic.png', upload_to='Profile_pic')
    
    def __str__(self):
        return f'{self.user.username}-Profile'