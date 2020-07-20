//----------------- Index Functions----------------//
$('#newworkout').click(function () {
  window.location = '/workouts/new';
});

$('#showmore').click(function () {
  window.location = '/workouts/';
});



//---------------------------Workout form Trainer---------------//

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
  if( document.getElementById("duplicator2") != null)
      numOfClicks++;
  if (numOfClicks <= 2) {
    var clone = original.cloneNode(true);
    clone.childNodes[9].childNodes[1].value = "";
    clone.childNodes[3].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_name";
    clone.childNodes[5].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_sets";
    clone.childNodes[7].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_reps";
    clone.childNodes[9].childNodes[1].name = "ex_" + (numOfClicks + 1) + "_desc";
    clone.id = "duplicator" + ((numOfClicks)+1);
    var txt = '<h6>Ex' + (numOfClicks +1 ) +  '</h6>';
    clone.childNodes[1].innerHTML = txt;
    clones.push(clone);
    original.parentNode.appendChild(clone);
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


//--------------------------------Delete warning-------------------//

