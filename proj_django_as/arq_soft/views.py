from django.shortcuts import render
from .models import Stations

# Create your views here.

def home(request):
    stations = Stations.objects.all()
    return render(request, 'arq_soft/home.html', {'stations': stations})