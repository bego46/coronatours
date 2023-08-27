function initMap() {
  // --- <<<<<<<< --- Definiendo Variables --- >>>>>>>> ---
  let directionsService = new google.maps.DirectionsService();
  let directionsRenderer = new google.maps.DirectionsRenderer();
  let center = new google.maps.LatLng(10.39698, - 75.50265)
  let start = document.getElementById("start");
  let end = document.getElementById("end");


  // --- <<<<<<<< --- Cree un cuadro delimitador con lados a ~150 km de distancia del punto central --- >>>>>>>> ---
  const defaultBounds = {
    north: center.lat + 0.15,
    south: center.lat - 0.15,
    east: center.lng + 0.15,
    west: center.lng - 0.15,
  };
  const startP = document.getElementById("start_p");
  const endP = document.getElementById("end_p");
  const options = {
    bounds: defaultBounds,
    componentRestrictions: { country: "co" },
    fields: ["address_components", "geometry", "icon", "name"],
    strictBounds: false,
  };

  const autocomplete = new google.maps.places.Autocomplete(start, options);
  const autocomplete2 = new google.maps.places.Autocomplete(end, options);

  autocomplete.setComponentRestrictions({
    country: ["co", "mx"],
  });

  autocomplete2.setComponentRestrictions({
    country: ["co", "mx"]
  })

  // --- <<<<<<<< --- creando el mapa --- >>>>>>>> ---
  const map = new google.maps.Map(document.getElementById("map"), {
    center: center,
    zoom: 12,
    mapTypeControl: false,
  });

  // --- <<<<<<<< --- Autocompletador de lugares para el buscador --- >>>>>>>> ---

  autocomplete.bindTo("bounds", map);

  autocomplete.addListener("place_changed", () => {

    const info = new google.maps.place.PlaceResult()
    const place = autocomplete.getPlace(info);

    if (!place.geometry || !place.geometry.location) { return; }

  });

  // --- <<<<<<<< --- Marca en el mapa la ruta --- >>>>>>>> ---
  directionsRenderer.setMap(map);
  const request = {
    origin: start.innerHTML,
    destination: end.innerHTML,
    travelMode: 'DRIVING',
  };
  directionsService.route(request, response => {
    directionsRenderer.setDirections(response);
    showSteps(response)
  });

};

function showSteps(directionResult) {
  const myRoute = directionResult.routes[0].legs[0];
  let distance = myRoute.distance
  let duration = myRoute.duration
  const dista = document.getElementById("distanceId").innerHTML = distance.value;
  const durat = document.getElementById("durationId").value = duration.value;
  // element.innerHTML = dista

  if (typeof (Storage) !== "undefined") {
    localStorage.setItem("distancia", dista);


  } else {
    console.log("LocalStorage no soportado en este navegador")
  }

  const ti = localStorage.getItem("distancia");
  const test = document.getElementById("v-store").value = ti;
  console.log(test);
  console.log(distance);
  console.log(dista);
  console.log(durat);
}

