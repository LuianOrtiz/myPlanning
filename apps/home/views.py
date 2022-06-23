from http.client import responses
from urllib import response
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')
