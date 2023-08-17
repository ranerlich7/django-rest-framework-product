from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    stock = models.IntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

