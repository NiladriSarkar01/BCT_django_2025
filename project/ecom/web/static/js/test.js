// function change() {
//   var x = document.getElementsByClassName("test");
//   x[0].setAttribute("src", "/static/res/guts.jpg");
//   return x[0].getAttribute("src");
// }

const x = document.getElementById("para");

window.addEventListener("scroll", () => {
  let ofset = window.scrollY;
  x.style.backgroundPositionY = ofset * 0.7 + "px";
});
