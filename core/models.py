from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    phone_number = models.CharField(max_length=15,unique=True)
    USERNAME_FIELD = "phone_number"
    address = models.CharField(max_length=50,null=True,blank=True)