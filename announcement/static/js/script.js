// Constants
const CLOCK_INTERVAL = 1000 * 1;
const AJAX_INTERVAL = 1000 * 60 * 5;
const SLIDE_SHOW_INTERVAL = 1000 * 10;

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
          var div = $('<div/>');
          div.addClass('ytplayer');
          item.data('youtube-url', data.slides[i].content);
          item.children('.carousel-data').append(div);
          break;
        case 1:
          var img = $('<img/>');
          img.attr('src', data.slides[i].content);
          img.addClass('slide-img');
          item.children('.carousel-data').append(img);
          break;
        case 2:
          item.children('.carousel-data').text(data.slides[i].content);
          break;
      }

      $('#mainSlide .carousel-inner').append(item);
    }

    if (window.ytAPIReady) {
      window.createPlayers();
    } else {
      window.slideContentReady = true;
    }
    console.log(data);
  }
  function onAnnouncements(data) {
    $('#Announcement').text(data.announcements.join(' | '));
    console.log(data);
  }
  function onLectures(data) {
    var a=data.lectures.length;
    var str="<h5>Bugünkü Dersler</h5>";
    for(var b=0;b<a;b++){
      str+=data.lectures[b].code+" "+data.lectures[b].name+" "+data.lectures[b].lecturer+" "+data.lectures[b].time+"<br>";
    }
    $('#Lectures').html(str);
     console.log(data);
  }
  function onExams(data) {
    var a=data.exams.length;
    var str="<h5>Yaklaşan Sınavlar</h5>";
    for(var b=0;b<a;b++){
      str+=data.exams[b].code+" "+data.exams[b].name+" "+data.exams[b].lecturer+" "+data.exams[b].datetime+" "+data.exams[b].location+" "+data.exams[b].duration+"<br>";
    }
    $('#Exams').html(str);
    console.log(data);
  }
  function onEvents(data) {
    var a=data.events.length;
    var str="<h5>Yaklaşan Etkinlikler</h5>";
    for(var b=0;b<a;b++){
      str+=data.events[b].datetime+" "+data.events[b].title+" "+data.events[b].location+"<br>";
    }
    $('#Events').html(str);
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

  function updateText() {
    $('#speed_text').text(speedFactor + " saniyede bir tur");
  }
  updateText();

  $("#scroll_speedup").click(function() {
    if (speedFactor > 1) {
      speedFactor --;
      updateText();
    }
    $("#Announcement").css('animation', "scrollleft " + speedFactor + "s linear infinite");
  });

  $("#scroll_speeddown").click(function() {
    speedFactor ++;
    updateText();
    $("#Announcement").css('animation', "scrollleft " + speedFactor + "s linear infinite");
  });
})(window);

// Settings
(function(window) {
  $(document.body).keydown(function() {
    if (event.which == 13) { // Enter tuşu
      $('#settingsModal').modal('show');
      event.preventDefault();
    }
  });
})(window);

// Date and Clock
(function(window) {
  setInterval(function() {
    $("#tarihsaat").html(new Date().toLocaleString());
  }, CLOCK_INTERVAL);
})(window);

// Slide Show
(function(window) {
  var players = [], playerReady = {};
  var autoSlideEnabled = false;

  window.createPlayers = createPlayers;
  window.onYouTubeIframeAPIReady = function() {
    if (window.slideContentReady) {
      window.createPlayers();
    } else {
      window.ytAPIReady = true;
    }
  }

  function createPlayers() {
    players = [];
    playerReady = {};

    $('.carousel-item').each(function() {
      var url = $(this).data('youtube-url');
      if (url) {
        var id = youtube_parser(url);
        if (id) {
          $(this).data('youtube-idx', players.length);
          $(this).find('.ytplayer').attr('id', 'ytplayer' + players.length);
          players.push(new YT.Player('ytplayer' + players.length, {
            videoId: id,
            playerVars: {
              'autoplay': 0,
              'controls': 0,
              'showinfo': 0,
              'rel': 0,
              'modestbranding': 1,
            },
            events: {
              'onReady': onPlayerReady,
              'onStateChange': onPlayerStateChange
            }
          }));
        }
      }
    });

    var idx = getYTIdx($('.carousel-item.active'));
    if (idx == undefined) {
      autoSlideEnabled = true;
      setTimeout(nextSlide, SLIDE_SHOW_INTERVAL);
    }
  }
  function onPlayerReady(event) {
    // Oynatıcı aktif slaytın ise oynat
    var parent = $(event.target.getIframe()).parents('.carousel-item');
    if (parent.hasClass('active')) {
      autoSlideEnabled = false;
      event.target.playVideo();
    }

    // Oynatıcı hazır bayrağını işaretle
    var idx = getYTIdx(parent);
    if (idx != undefined) {
      playerReady[idx] = true;
    }
  }
  function onPlayerStateChange(event) {
    switch (event.data) {
      case YT.PlayerState.PLAYING:
        var parent = $(event.target.getIframe()).parents('.carousel-item');
        if (!parent.hasClass('active')) { // slayt aktif değilse
          event.target.pauseVideo(); // durdur
          event.target.seekTo(0, true); // başa sar
        }
        break;
      case YT.PlayerState.ENDED:
        autoSlideEnabled = true;
        nextSlide();
        break;
      default:

    }
  }

  // Youtube api yükle
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // Slayt ayarları
  $('#mainSlide').carousel({
    interval: false, // Kendi kendine çalışmasın
    pause: false,
  });

  // Slayt geçiş yöneticisi
  function nextSlide() {
    if (autoSlideEnabled) {
      $('#mainSlide').carousel('next');
      setTimeout(nextSlide, SLIDE_SHOW_INTERVAL);
    }
  }

  // Slayt değiştiğinde
  $('#mainSlide').on('slid.bs.carousel', function(evt) {
    var idx = getYTIdx(evt.relatedTarget)
    if (idx != undefined && playerReady[idx]) {
      autoSlideEnabled = false;
      players[idx].playVideo();
    }
  });

  // Slaytın youtube player indisini bul
  function getYTIdx(elm) {
    var idx = parseInt($(elm).data('youtube-idx'));
    if (!isNaN(idx) && players[idx]) {
      return idx;
    }
  }

  // https://stackoverflow.com/questions/3452546/how-do-i-get-the-youtube-video-id-from-a-url
  function youtube_parser(url) {
    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*/;
    var match = url.match(regExp);
    return (match&&match[7].length==11)? match[7] : false;
  }
})(window);
