function openTab(header) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(header).style.display = "block";
}

function searchTitle() {
    title = document.getElementById("title").value
    
    //search for title amongst addonss
}


//document.getElementById("defaultOpen").click();

window.addEventListener('load', 
  function() { 
    document.getElementById("defaultOpen").click();
  }, false);