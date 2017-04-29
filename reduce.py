from flask import Flask, render_template as thing, redirect, request, url_for, abort, flash, session

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'



@app.route('/')
def index():
    return thing('index.html')




















if __name__ == '__main__':
 	app.run(debug=True, host='0.0.0.0')