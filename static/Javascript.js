(function() {
	var dropzone = document.getElementById('dropzone');
	var upload = function(files) { /*gets the file from data transfer array in function (e)*/
    var formData = new FormData(),
			/*this is what is gonna get passed via ajax to php, allows us to append to php*/
			xhr = new XMLHttpRequest(),
			x; /*allows us to open a request to upload and transfer to php*/
		for (x = 0; x < files.length; x++) { /* loops thru that files.length property to make function go over each file dropped*/
			formData.append('file[]', files[x]);
		}
		xhr.onload = function() { /*when transfer is good we want to parse data (json parsing)*/
			var data = this.responseText;
			console.log(data);
		}
		xhr.open('post', 'upload.')//JOSE! CHANGE THIS TO PYTHON IDK HOW LOL
		xhr.send(formData) // what data? FORMDATA!
	}
	dropzone.ondrop = function(e) {
		e.preventDefault();
		this.className = 'dropzone';
		upload(e.dataTransfer.files);
	}
    
    
    
	dropzone.ondragover = function() {
		this.className = 'dropzone dragover';
         var element = document.getElementById("text");
        element.innerHTML = "Drop it like it's hot";
        
		return false;
	};
	dropzone.ondragleave = function() {
		this.className = 'dropzone';
    
           var element = document.getElementById("text");
        element.innerHTML = "Drop File anywhere.";
		return false;
	};

}());
//WHEN FILE IS DRAGGED IT TRIGGERS UPLOAD.PHP BUT IT SAYS 404, MIGHT BE BC I DONT HAVE PHP, THE CONSOLE SHOULD LOG HELLO.