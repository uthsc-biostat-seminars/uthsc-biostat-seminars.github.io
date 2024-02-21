var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = panel.scrollHeight + "px";
      setTimeout(function(){panel.style.maxHeight = null;}, 50)
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
      setTimeout(function(){panel.style.maxHeight = "unset";}, 200)
    } 
  });
}