var myDropzone = new Dropzone("div #my-dropzone", { url: "/file/post"});
var dropzone = document.getElementById('my-dropzone');




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