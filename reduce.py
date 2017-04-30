
from flask import Flask, render_template as thing, redirect, request, url_for, abort, flash, session, send_from_directory
from werkzeug import secure_filename
import os
import subprocess


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'video/'

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4,' , 'tf', 'wmv', 'avi', 'flv'])




@app.route('/')
def index():
    return thing('index.html')



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
        return peggy(filename)
        # return redirect(url_for("compress", filename = filename))

    print 'Peggy Did not Run Son'
                               

def peggy(filename):
	output_name = changey(filename)
	subprocess.call('ffmpeg -i '+str(filename)+' -b 1000000 '+output_name, cwd=os.path.join(app.config['UPLOAD_FOLDER']), shell=True)
	return redirect(url_for("compress", filename=output_name))
	# subprocess.call('ffmpeg -r 10 -i frame%03d.png -r ntsc '+str(out_movie), shell=True)

def changey(filename):
	file = str(filename)
	splitter = file.split(".")
	rs = splitter[0][::-1]+"."+splitter[1]
	return rs


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







if __name__ == '__main__':

 	app.run(debug=True, host='0.0.0.0')
 	
 	

