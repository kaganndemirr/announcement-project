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
  }, 1000);
})(window);
