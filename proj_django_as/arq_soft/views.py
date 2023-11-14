from django.shortcuts import render
from django.http import JsonResponse
from .models import Stations

# Create your views here.

def home(request):
    stations = Stations.objects.all()
    return render(request, 'arq_soft/home.html', {'stations': stations})

#função para criar uma nova estação
def save_station(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        station = request.Post.get('station')
        station_name = request.POST.get('station_name')
        station_number = request.POST.get('station_number')

        # Crie uma nova instância do modelo Station e salve no banco de dados
        new_station = Station(lat=lat, lon=lon, station=station, station_name=station_name, station_number=station_number)
        new_station.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'})
