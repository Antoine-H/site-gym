var map = L.map('map', {fullscreenControl: true})
            .setView([47.28177112753235, -1.4819578444121362], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery &copy; <a href="http://mapbox.com">Mapbox</a>',
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiYXBqYiIsImEiOiJjaXl2anppM2UwMDU2MnFwMDI1dHptaGE5In0.VtUPSXqE3ujhmbtqInPiRQ'
}).addTo(map);

L.marker([47.28177112753235, -1.481957844121362]).addTo(map)
    .bindPopup('Salle du tremplin')
    .openPopup();

