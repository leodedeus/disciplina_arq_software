// Em seu_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Inicialize o mapa
    var map = L.map('map').setView([0, 0], 2);

    // Adicione uma camada de mapa (por exemplo, OpenStreetMap)
    //L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    //    attribution: 'OpenStreetMap'
    //}).addTo(map);

    // Adicione marcadores ao mapa
    stationsData.forEach(function (station) {
        var latLng = [station.lat, station.lon];
        L.marker(latLng).addTo(map);
    });
});
