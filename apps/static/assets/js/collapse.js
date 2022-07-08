/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
const burgerMenu = "fa fa-bars";
const cancelMenu = "fa fa-times";
function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
      if(window.innerWidth < 700){
        change_icon(burgerMenu);
      }
    } else {
      x.style.display = "block";
      if(window.innerWidth < 700){
        change_icon(cancelMenu);
      }
    }
  }

const change_icon = (clase) => {
    let divName = document.getElementById("change-icon")
    divName.className = clase;
}
