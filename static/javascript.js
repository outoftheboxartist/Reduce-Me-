new Dropzone(document.getElementById("myAwesomeDropzone"), { 
    url: "google.com", // Set the url
    previewsContainer: "#previews",
      addRemoveLinks: true,
      init: function() {
          
      }
    
    
   
 });

var dropzone = document.getElementById('myAwesomeDropzone');



dropzone.ondragover = function() {
    this.className = 'drag';
	var element = document.getElementById("text");
	element.innerHTML = "Drop it like it's hot";
	return false;
};


dropzone.ondragleave = function() {
     dropzone.classList.remove('drag');
     dropzone.classList.add("box1");
   
	var element = document.getElementById("text");
	element.innerHTML = "Drop File anywhere.";
	return false;
};

dropzone.ondrop = function(){ 
    dropzone.classList.remove('drag');
    dropzone.classList.add("box1");
    var element = document.getElementById("text");
	element.innerHTML = "Drop File anywhere.";
	return false;
};

