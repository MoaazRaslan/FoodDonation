from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('evaluator','Evaluator'),
        ('supervisor','Supervisor'),
        ('admin','Admin'),
        ('restaurant','Restaurant'),
    )
    name = models.CharField(max_length=20,choices=ACCOUNT_TYPE_CHOICES)

    def __str__(self):
        return self.name

class City(models.Model):
    CITY_CHOICES = (
        ('aleppo','Aleppo'),
        ('damascus','Damascus')
    )
    name = models.CharField( max_length=50, choices=CITY_CHOICES)
    def __str__(self):
        return self.name
    

class User(AbstractUser):

    #common between employee and restaurant
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name='users')
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255,blank=True,null=True)
    trusted = models.BooleanField(default=False)
    city = models.ForeignKey(City,on_delete=models.PROTECT,related_name='users')
    def __str__(self):
        return self.username

