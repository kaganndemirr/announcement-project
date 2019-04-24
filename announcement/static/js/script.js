function init() {
  $.get("/ajax/weather", function(weather) {
    $('#weather_forecast').text(weather.Trabzon);
  });
}

init();
