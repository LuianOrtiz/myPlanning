from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Memberhsip(models.Model):
    pass

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)