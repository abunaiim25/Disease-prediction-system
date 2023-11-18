from django.shortcuts import render
from django.contrib import messages
from .models import *


# Create your views here.

def home(request):
    return render(request, 'store/index.html')


def support(request):
    return render(request, 'store/support.html')

def about_app(request):
    return render(request, 'store/about_app.html')

def history(request):
    return render(request, 'store/history.html')
