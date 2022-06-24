from django.shortcuts import render
from apps.todolist.models import List, Task, Step
# Create your views here.
def index(request):
    listas = List.objects.all()
    return render(request, 'todolist/index.html', {"tasks:": listas})
