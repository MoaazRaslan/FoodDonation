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


class User(AbstractUser):

    #common between employee and restaurant
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name='users')
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.username
