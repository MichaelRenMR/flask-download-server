from flask import Flask, send_from_directory, abort
from flask_autoindex import AutoIndex
import os.path

app = Flask(__name__)

# Server folder containing uploads
app.config['UPLOAD_FOLDER'] = '/home/michael/Desktop/Su22/clientserverDemo/server/uploads'  # TODO: Change me

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/uploads/<path:filename>', methods=['GET'])
def get_file(filename):
	try:
		return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
	except FileNotFoundError:
		abort(404)


# Convenience method for viewing uploads folder
index = AutoIndex(app, app.config['UPLOAD_FOLDER'], add_url_rules=False)
@app.route('/uploads/')
def autoindex():
	return index.render_autoindex('.')






# Server configs
# TODO: Change me
if __name__ == '__main__':
    app.run(host='127.0.0.1',port = 5000, threaded = True, debug = True)




