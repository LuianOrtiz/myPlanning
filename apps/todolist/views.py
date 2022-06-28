from django.shortcuts import render, redirect
from apps.todolist.models import List

# Create your views here.
def index(request):
    lists = List.objects.all()
    context = {
        "lists": lists
    }
    return render(request, 'todolist/index.html', context)

def create_list(request):
    list = List(name=request.POST['name'])
    list.save()
    return redirect('/todolist/')
