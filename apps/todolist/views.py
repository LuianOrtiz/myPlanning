from django.shortcuts import render
from django import template
# Create your views here.
def index(request):
    return render(request, 'todolist/index.html')
