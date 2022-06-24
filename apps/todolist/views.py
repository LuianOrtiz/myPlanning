from multiprocessing import context
from django.shortcuts import render
from apps.todolist.models import List, Task, Step
# Create your views here.
def index(request):
    lists = List.objects.all()
    tasks = Task.objects.all()
    context = {
        "lists": lists,
        "tasks": tasks
    }
    return render(request, 'todolist/index.html', context)
