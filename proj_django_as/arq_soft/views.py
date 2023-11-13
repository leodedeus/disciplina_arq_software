from django.shortcuts import render
#from .models import Stations

# Create your views here.

def home(request):
    return render(request, "arq_soft/home.html")

'''
def mapa(request):
    # Recupere os dados da tabela 'stations'
    stations_data = Stations.objects.values('lat', 'lon')

    # Converta os dados para uma lista de dicionários
    stations_list = list(stations_data)

    return render(request, 'home.html', {'stations_data': stations_list})
'''