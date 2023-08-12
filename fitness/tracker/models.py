from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        ('1', 'Admin'),
        ('2', 'Trainer'),
        ('3', 'Customer'),
    )
    user_type = models.CharField(choices=USER, max_length = 50, default = 1)
    
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
class Activity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    
    def __str__(self):
        return self.session_start + " to " + self.session_end
    
class Customer(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    address = models.TextField()   
    activity_id = models.ForeignKey(Activity,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Trainer(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    contactNo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.admin.first_name
    