from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


# Create your models here.

class List(models.Model):
    list_name = CharField(max_length=60)
    user = models.OneToOneField(User)

class Task(models.Model):
    task = CharField(max_length=180)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    finalized = models.DateField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

class Steps(models.Model):
    step = CharField(max_length=180)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
