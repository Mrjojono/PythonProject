// Initialisation de la carte
var map = L.map('map').setView([51.505, -0.09], 13);

// Récupération des champs d'entrée avec des valeurs par défaut
var nom = document.getElementById('nom') ? document.getElementById('nom').value : 'Nom par défaut';
var prenom = document.getElementById('prenom') ? document.getElementById('prenom').value : 'Prénom par défaut';
var latitude = document.getElementById('latitude') ? document.getElementById('latitude').value : '51.505';
var longitude = document.getElementById('longitude') ? document.getElementById('longitude').value : '-0.09';

// Conversion des coordonnées en flottants (au cas où elles seraient des chaînes de caractères)
latitude = parseFloat(latitude);
longitude = parseFloat(longitude);

// Ajout des tuiles OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Ajout d'un marqueur à la position par défaut
var marker = L.marker([latitude, longitude]).addTo(map);

// Contenu du popup par défaut
var popupContent = `
    <b>${nom}</b><br>
    ${prenom}<br>
    Latitude : ${latitude}<br>
    Longitude : ${longitude}
`;
marker.bindPopup(popupContent).openPopup();

// Gérer les clics pour déplacer le marqueur et ajouter une popup
map.on('click', function (e) {
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;

    // Mise à jour du marqueur
    marker.setLatLng([lat, lng]);

    // Mise à jour du contenu du popup
    var popupContent = `
        <b>${nom}</b><br>
        ${prenom}<br>
        Latitude : ${lat}<br>
        Longitude : ${lng}
    `;
    marker.bindPopup(popupContent).openPopup();

    // Centrer la carte sur le marqueur
    map.setView([lat, lng], 13);
});
