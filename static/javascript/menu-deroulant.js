function myFunction() {
    document.getElementById("fonction-bouton").classList.toggle("montrer");
}
window.onclick = function(event) {
  if (!event.target.matches('.bouton')) {

    var dropdowns = document.getElementsByClassName("contenu-menu-deroulant");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('montrer')) {
        openDropdown.classList.remove('montrer');
      }
    }
  }
}
