function onDropLeftDivClick(id) {
  closeAllDropDownMenu()
  document.getElementById(id).classList.toggle("show");
}
function closeAllDropDownMenu() {
  var dropdowns = document.getElementsByClassName("dropdown-content");
  var i;
   for (i = 0; i < dropdowns.length; i++) {
     var openDropdown = dropdowns[i];
     if (openDropdown.classList.contains('show')) {
       openDropdown.classList.remove('show');
     }
   }
}
window.onclick = function(event) {
  if (!event.target.matches('.drop-left-menu-ref')) {
    closeAllDropDownMenu()
  }
}
function showDialog(id, title, data){
  dialog = document.getElementById(id);
  dialog.getElementsByClassName("dialog_viewport")[0].innerHTML = data;
  dialog.getElementsByClassName("title")[0].innerHTML = title;
  if(!dialog.classList.contains("my-dialog-open"))
  dialog.classList.remove("my-dialog-close");
  dialog.classList.add("my-dialog-open");
}

function closeDialog(id){
  dialog = document.getElementById(id);
  dialog.classList.remove("my-dialog-open");
  dialog.classList.add("my-dialog-close");
}
