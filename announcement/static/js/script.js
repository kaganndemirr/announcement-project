// Constants
const CLOCK_INTERVAL = 1000 * 1;
const AJAX_INTERVAL = 1000 * 60 * 5;
var SLIDE_SHOW_INTERVAL = 1000 * 15;

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
    //console.log(data);
  }
  function onAnnouncements(data) {
    $('#Announcement').text(data.announcements.join(' | '));
    //console.log(data);
  }
  function onLectures(data) {
    var str = "";
    for(var b=0;b<data.lectures.length;b++){
      str+="<b>"+data.lectures[b].code+" "+data.lectures[b].name + "</b> <br>";
      str+="<i>"+data.lectures[b].lecturer+" "+data.lectures[b].location + "</i> <br>";
      str+=data.lectures[b].time+" "+data.lectures[b].duration+"<br><br>";
    }

    $('#Lectures').html(str);
    //console.log(data);
  }
  function onExams(data) {
    var str="";
    for(var b=0;b<data.exams.length;b++){
      str+="<b>"+data.exams[b].code+" "+data.exams[b].name + "</b> <br>";
      str+="<i>"+data.exams[b].lecturer+" "+data.exams[b].location + "</i> <br>";
      str+=data.exams[b].datetime+" "+data.exams[b].duration+"<br><br>";
    }
    $('#Exams').html(str);
    //console.log(data);
  }
  function onEvents(data) {
    var str="";
    for(var b=0;b<data.events.length;b++){
      str+="<b>"+data.events[b].datetime+"</b> "+data.events[b].title+" <i>"+data.events[b].location+"</i><br>";
    }
    $('#Events').html(str);
    //console.log(data);
  }
  function onWeather(data) {
    var img = $('<img class="img-fluid">');
    img.attr('src', data.icon);
    $('#uptime').html("Güncellenme Zamanı: "+new Date().toLocaleString());
    $('#weather_forecast').html(data.text);
    $('#humidity').html("Nem: "+data.humidity);
    $('#temp').html("Sıcaklık: "+data.temperature);
    $('#wind').html("Rüzgar: "+data.wind);
    $('#sunr').html("Gündoğumu: "+data.sunrise);
    $('#suns').html("Günbatımı: "+data.sunset);
    $('#weather_forecast').append(img);

    //console.log(data);
  }
})(window);

// Scroll Text
(function(window) {
  var speedFactorhorizontal = 15;
  var speedFactorvertical=15;
  function updateText() {
    $('#speed_text').html(speedFactorhorizontal + " saniyede bir yatay tur"+ "<br>"+speedFactorvertical+" saniyede bir dikey tur"+"<br>"+SLIDE_SHOW_INTERVAL/1000+" saniyede slayt geçiş hızı"+"<br>");
  }
  loadSettings();
  updateText();

  $("#scroll_speeduph").click(function() {
    if (speedFactorhorizontal > 1) {
      speedFactorhorizontal --;
      updateText();
      saveSettings();
    }
    $("#Announcement").css('animation', "scrollleft " + speedFactorhorizontal + "s linear infinite");
  });

  $("#scroll_speeddownh").click(function() {
    speedFactorhorizontal ++;
    updateText();
    saveSettings();
    $("#Announcement").css('animation', "scrollleft " + speedFactorhorizontal + "s linear infinite");
  });

  $("#scroll_speedupv").click(function() {
    if (speedFactorvertical > 1) {
      speedFactorvertical --;
      updateText();
      saveSettings();
    }
    $("#Lectures").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
    $("#Exams").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
    $("#Events").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
  });

  $("#scroll_speeddownv").click(function() {
    speedFactorvertical ++;
    updateText();
    saveSettings();
    $("#Lectures").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
    $("#Exams").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
    $("#Events").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
  });

  $("#slidespeedup").click(function() {
    if (SLIDE_SHOW_INTERVAL > 1000) {
      SLIDE_SHOW_INTERVAL -=1000;
      updateText();
      saveSettings();
    }
  });

  $("#slidespeeddown").click(function() {
    SLIDE_SHOW_INTERVAL +=1000;
    updateText();
    saveSettings();
  });

  function loadSettings() {
    var settings = localStorage.getItem('settings');
    if (settings) {
      settings = JSON.parse(settings);
      speedFactorhorizontal = settings.speedFactorhorizontal;
      speedFactorvertical = settings.speedFactorvertical;
      SLIDE_SHOW_INTERVAL = settings.SLIDE_SHOW_INTERVAL;
      $("#Announcement").css('animation', "scrollleft " + speedFactorhorizontal + "s linear infinite");
      $("#Lectures").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
      $("#Exams").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
      $("#Events").css('animation', "scrollup " + speedFactorvertical + "s linear infinite");
    }
  }

  function saveSettings() {
    var settings = {
      speedFactorhorizontal: speedFactorhorizontal,
      speedFactorvertical: speedFactorvertical,
      SLIDE_SHOW_INTERVAL: SLIDE_SHOW_INTERVAL,
    };
    localStorage.setItem('settings', JSON.stringify(settings));
  }
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
