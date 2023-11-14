//Cria o mapa leaflet
var coordinicio = [-15.794092, -47.882842];
var zoominicio = 13;

var map = L.map('map').setView(coordinicio, zoominicio);

//Adiciona o mapa base
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Função para adicionar marcadores ao mapa
function addMarkers(map, stations) {
    stations.forEach(function(station) {
        L.marker([station.lat, station.lon])
            .addTo(map)
            .bindPopup("Estação: " + station.station);
    });
}

// Chama a função addMarkers para adicionar os marcadores ao mapa
addMarkers(map, stations);