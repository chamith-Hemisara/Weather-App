document.addEventListener("DOMContentLoaded", function () {
  const locationInput = document.getElementById("locationInput");
  const suggestionsList = document.getElementById("suggestions");
  const map = L.map("map").setView([0, 0], 2); // Set the initial map view

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

  // Create a marker to indicate the selected location
  let marker;

  map.on("click", function (e) {
    const lat = e.latlng.lat.toFixed(6);
    const lon = e.latlng.lng.toFixed(6);
    locationInput.value = `Lat: ${lat}, Lon: ${lon}`;
    if (marker) {
      map.removeLayer(marker);
    }
    marker = L.marker(e.latlng).addTo(map);
  });

  locationInput.addEventListener("input", function () {
    // Clear the suggestions list
    suggestionsList.innerHTML = "";
    // Remove the marker when the input changes
    if (marker) {
      map.removeLayer(marker);
    }
  });

  locationInput.addEventListener("change", function () {
    const locationText = locationInput.value;
    const [lat, lon] = locationText.split(',').map(item => parseFloat(item.replace(/\D/g, '')));

    if (!isNaN(lat) && !isNaN(lon)) {
      map.setView([lat, lon], 13);
      if (marker) {
        map.removeLayer(marker);
      }
      marker = L.marker([lat, lon]).addTo(map);
    }
  });
});
