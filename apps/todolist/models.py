from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class List(models.Model):
    name = models.CharField(blank=False,default= 'Nueva Lista', max_length=60)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(blank=False,default='Nueva Tarea',max_length=180)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    finalized = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Step(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(blank=False,default= 'Nuevo Paso', max_length=180)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
