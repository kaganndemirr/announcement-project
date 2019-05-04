// Constants
const CLOCK_INTERVAL = 1000 * 1;
const AJAX_INTERVAL = 1000 * 60 * 5;

// Ajax Requests
(function(window) {
  function updateAjax() {
    $.get('/ajax/slides', onSlides);
    $.get('/ajax/announcements', onAnnouncements);
    $.get('/ajax/lectures', onLectures);
    $.get('/ajax/exams', onExams);
    $.get('/ajax/events', onEvents);
    $.get('/ajax/weather', onWeather);
  }
  updateAjax();
  setInterval(updateAjax, AJAX_INTERVAL);

  // Ajax Responses
  function onSlides(data) {
    console.log(data);
  }
  function onAnnouncements(data) {
    console.log(data);
  }
  function onLectures(data) {
    console.log(data);
  }
  function onExams(data) {
    console.log(data);
  }
  function onEvents(data) {
    console.log(data);
  }
  function onWeather(data) {
    var img = $('<img>');
    img.attr('src', data.icon);
    $('#weather_forecast').text(data.text);
    $('#weather_forecast').append(img);

    console.log(data);
  }
})(window);

// Scroll Text
(function(window) {
  var speedFactor = 10;

  $("#scroll_speedup").click(function() {
    if (speedFactor > 1) {
      speedFactor --;
    }

    $("#scroll_text").css('animation', "scroll " + speedFactor + "s linear infinite");
  });

  $("#scroll_speeddown").click(function() {
    speedFactor ++;

    $("#scroll_text").css('animation', "scroll " + speedFactor + "s linear infinite");
  });
})(window);

// Clock
(function(window) {
  setInterval(function() {
    $("#tarihsaat").html(new Date().toLocaleString());
  }, CLOCK_INTERVAL);
})(window);
