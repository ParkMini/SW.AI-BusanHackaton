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
}

function crashDetection() {
  $.ajax({
    url: `./crashDetection`,
    method: `GET`,
  });
}

function busNumDetection(num) {
  $.ajax({
    url: `./busNumDetection/${num}`,
    method: `GET`,
  });
}

function dotDetection() {
  $.ajax({
    url: `./dotDetection`,
    method: `GET`,
  });
}

function manyHumanDetection() {
  $.ajax({
    url: `./manyHumanDetection`,
    method: `GET`,
  });
}

function useDayDetection() {
  $.ajax({
    url: `./useDayDetection`,
    method: `GET`,
  });
}