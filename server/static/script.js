function noDetection() {
  $.ajax({
    url: `./noDetection`,
    method: `GET`,
  });
}

function humanDetection(name) {
  $.ajax({
    url: `./humanDetection/${name}`,
    method: `GET`,
  });
  if (name == "CSeungJoo") {
    var audio = new Audio("/static/music/friendCSeungJoo.mp3");
  } else {
    var audio = new Audio("/static/music/friendGunggme.mp3");
  }
  audio.play();
}

function crashDetection() {
  $.ajax({
    url: `./crashDetection`,
    method: `GET`,
  });
  var audio = new Audio("/static/music/crashDetection.mp3");
  audio.play();
}

function busNumDetection(num) {
  $.ajax({
    url: `./busNumDetection/${num}`,
    method: `GET`,
  });
  if (num == 1008) {
    var audio = new Audio("/static/music/1008.mp3");
  } else if (num == 518) {
    var audio = new Audio("/static/music/518.mp3");
  } else if (num == 3003) {
    var audio = new Audio("/static/music/3003.mp3");
  } else if (num == 74) {
    var audio = new Audio("/static/music/74.mp3");
  } else if (num == 4101) {
    var audio = new Audio("/static/music/4101.mp3");
  }
  audio.play();
}

function dotDetection() {
  $.ajax({
    url: `./dotDetection`,
    method: `GET`,
  });
  var audio = new Audio("/static/music/dotDetection.mp3");
  audio.play();
}

function manyHumanDetection() {
  $.ajax({
    url: `./manyHumanDetection`,
    method: `GET`,
  });
  var audio = new Audio("/static/music/manyHumanDetection.mp3");
  audio.play();
}

function useDayDetection() {
  $.ajax({
    url: `./useDayDetection`,
    method: `GET`,
  });
  var audio = new Audio("/static/music/useDayDetection.mp3");
  audio.play();
}
