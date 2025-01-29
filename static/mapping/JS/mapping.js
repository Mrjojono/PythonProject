// Initialisation de la carte
var map = L.map('map').setView([51.505, -0.09], 13);


// Ajout des tuiles OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Ajout d'un marqueur à la position par défaut
var latitude = 50
var longitude = 45
var marker = L.marker([latitude, longitude]).addTo(map);


// Gérer les clics pour déplacer le marqueur et ajouter une popup
map.on('click', function (e) {
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;

    // Mise à jour du marqueur
    marker.setLatLng([lat, lng]);

    // Mise à jour du contenu du popup
    var popupContent = `
        Latitude : ${lat}<br>
        Longitude : ${lng}
    `;
    marker.bindPopup(popupContent).openPopup();

    // Centrer la carte sur le marqueur
    map.setView([lat, lng], 13);
});
