from flask import Flask, render_template as thing, redirect, request, url_for, abort, flash, session, send_from_directory
from ffmpy import FFmpeg as god
from werkzeug import secure_filename
import os
import subprocess

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'video/'

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4,' , 'tf', 'wmv', 'avi', 'flv'])








@app.route('/')
def index():
    return thing('index.html')


# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
# 	if request.method == 'POST':
# 		if 'file' not in request.files:
# 			flash('No file part')
# 			return redirect(request.url)
		

#         stream_file = request.files['file']

#         ff = god(
#             inputs={'pipe:0': None},
#             outputs={'pipe:1': '-f mp4'}
#         )
#         stdout, stderr = ff.run(input_data=stream_file.read('mov'), stdout=subprocess.PIPE)
#         return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''
	
    	
   # if request.method == 'POST':
   #    f = request.files['file']
   #    f.save(secure_filename(f.filename))
   #    videoReduce(f.filename)
   #    return 'file uploaded successfully'

# Route that will process the file upload
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # file.save(filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        print 'gotfile'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print 'gotfile2222222222222222222222222222222222222222'
        return redirect(url_for("compress", filename = filename))

    print 'got no file'
                               




@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/compress/<filename>')
def compress(filename):
    return thing("compress.html", filename = filename)




# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']





def videoReduce(input):
	box = god(inputs={input: None}, outputs={'output.mp4': '-f mp4'})
	box.cmd
	box.run
	return 0







if __name__ == '__main__':
 	app.run(debug=True, host='0.0.0.0')