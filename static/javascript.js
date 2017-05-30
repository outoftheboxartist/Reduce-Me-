new Dropzone(document.getElementById("myAwesomeDropzone"), {
  url: "/upload", // Set the url
  previewsContainer: "#previews",
  addRemoveLinks: true,
  maxFiles: 1,
  maxFilesize: 20000,
  createImageThumbnails: true,
  //renameFilename: , //leaving this open, we need it to be unique enough
  dictRemoveFile: 'Click to Remove this file NOW!',
  dictCancelUploadConfirmation: 'File has been removed B',
  dictCancelUpload: 'File has been canceled B',
  dictMaxFilesExceeded: 'We will only work on 1 file not multiple',
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

dropzone.ondrop = function() {
  dropzone.classList.remove('drag');
  dropzone.classList.add("box1");
  var element = document.getElementById("text");
  element.innerHTML = "Drop File anywhere.";
  return false;
};
