var dataurl = 'geodata/data.geojson';
var lon = -114;
var lat = 51;
var zoom = 10;
var map, layer;

map = new L.map('map').setView([lat, lon], zoom);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19,
}).addTo(map);


// Download GeoJSON data with Ajax
fetch(dataurl)
    .then(function(resp) {
    return resp.json();
})
.then(function(data) {
    L.geoJson(data, {
         onEachFeature: function onEachFeature(feature, layer) {
            var props = feature.properties;
            var content = `<h3>${props.name}</h3>`;
            layer.bindPopup(content);
      }}).addTo(map);
});

  function map_init(map_div) {
       var tileMapQuest = L.tileLayer('http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
     subdomains: ['otile1','otile2','otile3','otile4'],
     attribution: 'Map tiles by <a href="http://open.mapquestapi.com/">MapQuest</a>. Data &copy; by <a href="http://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>.',
     maxZoom: 18
       });
       var map_layers = [tileMapQuest];
       var map = L.map('leaflet-container', {
         center: [{{ lat }}, {{ lon }}],
         zoom: 10,
         layers: map_layers,
         worldCopyJump: false
       });
       {% if features %}
         {% for feat in features %}
           var feature = new L.geoJson({{ feat.geometry.geojson|safe }}).addTo(map);
         {% endfor %}
       {% endif %}
    }


      window.addEventListener("map:init", function (e) {
          var detail = e.detail;
          L.marker([50.5, 30.5]).addTo(detail.map);
      }, false);