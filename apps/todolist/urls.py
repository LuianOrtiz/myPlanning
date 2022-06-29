from django.urls import path
from apps.todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newlist/', views.create_list, name='create_list'),
    path('task/<int:id>/', views.list_task, name='list_task'),
]