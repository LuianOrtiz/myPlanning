import imp
from django.urls import path
from apps.todolist import views

urlpatterns = [
    path('', views.index, name='index')
]