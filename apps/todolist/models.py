from django.db import models


# Create your models here.

class List(models.Model):
    list_name = models.CharField(blank=False, default= '', max_length=60)
    
    def __str__(self):
        return self.list_name
    

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    task = models.CharField(blank=False, default= '',max_length=180)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    finalized = models.DateField(null=True)

    def __str__(self):
        return self.task
    

class Step(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    step = models.CharField(blank=False, default= '', max_length=180)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.step
    
