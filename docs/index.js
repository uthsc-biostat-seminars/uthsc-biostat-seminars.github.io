/* const accordion = document.getElementsByClassName('container');

for (i=0; i<accordion.length; i++) {
  accordion[i].addEventListener('click', function () {
    this.classList.toggle('active')
  })
}*/

document.addEventListener('DOMContentLoaded', function () {
  const accordions = document.querySelectorAll('.accordion .container');

  accordions.forEach(function (accordion) {
    accordion.addEventListener('click', function (event) {
      // This stops the event from bubbling up to parent accordions
      event.stopPropagation();

      // Toggle 'active' class
      this.classList.toggle('active');
    });
  });
});