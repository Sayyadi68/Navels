// slider 1
function Previous1( ) {
    document.getElementById("slider1").scrollBy(-315,0);
}
function Next1() {
    document.getElementById("slider1").scrollBy(315,0);
}

// slider 2
function Previous2( ) {
    document.getElementById("slider2").scrollBy(-315,0);
}
function Next2() {
    document.getElementById("slider2").scrollBy(315,0);
}

// slider 3
function Previous3( ) {
    document.getElementById("slider3").scrollBy(-315,0);
}
function Next3() {
    document.getElementById("slider3").scrollBy(315,0);
}


let isDown = false;
let startX;
let scrollLeft;
const slider = document.querySelector('.items');

const end = () => {
	isDown = false;
  slider.classList.remove('active');
}

const start = (e) => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX || e.touches[0].pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;	
}

const move = (e) => {
	if(!isDown) return;

  e.preventDefault();
  const x = e.pageX || e.touches[0].pageX - slider.offsetLeft;
  const dist = (x - startX);
  slider.scrollLeft = scrollLeft - dist;
}

(() => {
	slider.addEventListener('mousedown', start);
	slider.addEventListener('touchstart', start);

	slider.addEventListener('mousemove', move);
	slider.addEventListener('touchmove', move);

	slider.addEventListener('mouseleave', end);
	slider.addEventListener('mouseup', end);
	slider.addEventListener('touchend', end);
})();
