// When the user clicks on user profile
//toggle between hiding and showing the dropdown content
function profile_options() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      let dropdowns = document.getElementsByClassName("dropdown-content");
      let i;
      for (i = 0; i < dropdowns.length; i++) {
        let openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

/* Highlight current page*/
const theactivePage = window.location.pathname;
let navLinks = document.querySelectorAll('nav a').forEach(link => {
  if(link.href.includes(`${theactivePage}`)) {
    link.classList.add('active');
  }
})

/*
let links = document.querySelectorAll('nav a');
let sectionId = document.querySelector('section').id;

for (let link in links){
  link.classList.add("active");
}
*/