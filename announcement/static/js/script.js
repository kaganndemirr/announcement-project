// Constants
const CLOCK_INTERVAL = 1000 * 1;
const AJAX_INTERVAL = 1000 * 60 * 5;

// Templates
var tplSlide = $('#slideItemTpl').html();

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
    $('#mainSlide .carousel-inner').html('');

    var item;

    for (var i=0; i<data.slides.length; i++) {
      item = $('<div/>');
      item.html(tplSlide);
      item.addClass('carousel-item');
      if (i == 0)
        item.addClass('active');
      item.children('.carousel-caption').text(data.slides[i].title)
      switch(data.slides[i].type) {
        case 0:
          item.children('.carousel-data').text(data.slides[i].content);
          // TODO youtube video ekle
          break;
        case 1:
          var img = $('<img/>');
          img.attr('src', data.slides[i].content);
          item.children('.carousel-data').append(img);
          break;
        case 2:
          item.children('.carousel-data').text(data.slides[i].content);
          break;
      }


      $('#mainSlide .carousel-inner').append(item);
    }

    console.log(data);
  }
  function onAnnouncements(data) {
    $('#Announcement').text(data.announcements.join(' | '));
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
    $('#uptime').html("Güncellenme Zamanı: "+new Date().toLocaleString());
    $('#weather_forecast').html(data.text);
    $('#humidity').html("Nem: "+data.humidity);
    $('#temp').html("Sıcaklık: "+data.temperature);
    $('#wind').html("Rüzgar: "+data.wind);
    $('#sunr').html("Gündoğumu: "+data.sunrise);
    $('#suns').html("Günbatımı: "+data.sunset);
    $('#weather_forecast').append(img);

    console.log(data);
  }
})(window);

// Scroll Text
(function(window) {
  var speedFactor = 10;
  document.getElementById("speed").innerHTML =speedFactor+" seconds per tour";
  $("#scroll_speedup").click(function() {
    if (speedFactor > 1) {
      speedFactor --;
      document.getElementById("speed").innerHTML =speedFactor+" seconds per tour";
    }
    $("#Announcement").css('animation', "scroll " + speedFactor + "s linear infinite");
  });

  $("#scroll_speeddown").click(function() {
    speedFactor ++;
    document.getElementById("speed").innerHTML =speedFactor+" seconds per tour";
    $("#Announcement").css('animation', "scroll " + speedFactor + "s linear infinite");
  });
})(window);

// Date and Clock
(function(window) {
  setInterval(function() {
    $("#tarihsaat").html(new Date().toLocaleString());
  }, CLOCK_INTERVAL);
})(window);
