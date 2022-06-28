from django.urls import path
from apps.todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newlist/', views.create_list, name='create_list'),
]