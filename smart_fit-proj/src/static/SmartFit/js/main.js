//----------------- Index Functions----------------//
$('#newworkout').click(function () {
  window.location = '/workouts/new';
});

$('#showmore').click(function () {
  window.location = '/workouts/';
});



//---------------------------Workout form Trainer---------------//

if( document.getElementById("duplicator3") != null)
    var updateClicks = 3;

if( document.getElementById("duplicator2") != null)
      var updateClicks = 2;
else
    var updateClicks = 1;


var numOfClicks = 1;
var original = document.getElementById("duplicator1");
if (original != null)
  var clones = [original];

var numOfClicks = 1;
var original = document.getElementById("duplicator1");
if (original != null)
  var clones = [original];

$(".addNewEx").click(function () {
  if (numOfClicks <= 2) {

    var clone = original.cloneNode(true);
    clone.childNodes[9].childNodes[1].value = "";
    clone.childNodes[3].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_name";
    clone.childNodes[5].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_sets";
    clone.childNodes[7].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_reps";
    clone.childNodes[9].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_desc";
    clone.id = "duplicator" + ((numOfClicks++)+1);
    var txt = '<h6>Ex' + (numOfClicks ) +  '</h6>';
    clone.childNodes[1].innerHTML = txt;
    clones.push(clone);
    original.parentNode.appendChild(clone);
  }
})



$(".createmore").click(function () {


  if (updateClicks <= 2) {
    var clone = original.cloneNode(true);
    clone.childNodes[9].childNodes[1].value = "";
    clone.childNodes[3].childNodes[1].name = "ex_" + (updateClicks + 1) + "_name";
    clone.childNodes[5].childNodes[1].name = "ex_" + (updateClicks + 1) + "_sets";
    clone.childNodes[7].childNodes[1].name = "ex_" + (updateClicks + 1) + "_reps";
    clone.childNodes[9].childNodes[1].name = "ex_" + (updateClicks + 1) + "_desc";
    clone.id = "duplicator" + ((updateClicks)+1);
    var txt = '<h6>Ex' + (updateClicks +1 ) +  '</h6>';
    clone.childNodes[1].innerHTML = txt;
    clones.push(clone);
    original.parentNode.appendChild(clone);
    updateClicks += 1;
  }
})


//------------------------------AJAX------------------------------//
const $exList = $(".exercises-list");
if ($exList.find('option').length == 1) {
  $.getJSON("/workouts/exercises", function (data) {
    $.each(data, function (key, item) {
      $exList.append(
        $(`<option value="${item.name}">${item.name}</option>`)
      )
    });
  });
}



