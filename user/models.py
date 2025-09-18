from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name='users')

    def __str__(self):
        return self.username
