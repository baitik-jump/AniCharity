from django.shortcuts import render
from .models import Tops

def index(request):
    return render(request, 'main/head.html')

def abouUS(request):
    return render(request, 'main/AboutUs.html')

def tops(request):
    tops = Tops.objects.all()
    return render(request, 'main/tops.html', {'tops': tops})

def forum(request):
    return render(request, 'main/forum.html')
# Create your views here.
