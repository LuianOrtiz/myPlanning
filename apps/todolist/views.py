from django.shortcuts import render, redirect
from apps.todolist.models import List, Task

# Create your views here.
def index(request):
    lists = List.objects.all()
    context = {
        "lists": lists
    }
    return render(request, 'todolist/base.html', context)

def create_list(request):
    list = List(name=request.POST['name'])
    list.save()
    return redirect('/todolist/')

def list_task(request, id):
    tasks = Task.objects.filter(list=id)
    context = {
        "tasks": tasks
    }
    return render(request, 'todolist/list_task.html', context)