import requests
import errno
import os
import subprocess

# remote server upload URL
URL = 'http://127.0.0.1:5000/uploads/'  # TODO: Change me

# name of file to be downloaded
FILENAME =  'hello_server.py'  # TODO: Change me

# client directory for file to be downloaded to
LOCAL_DIR = os.path.abspath(os.getcwd())  # TODO: Change me
DOWNLOAD_DIR = os.path.join(LOCAL_DIR, 'downloads')

FILEPATH = os.path.join(DOWNLOAD_DIR, FILENAME)

# command to run the file locally
COMMAND = 'python ' + FILEPATH  # TODO: Change me

response = requests.get(URL+FILENAME)

if response.status_code == 404:
	raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), FILENAME)

with open(FILEPATH, 'wb') as f:
	f.write(response.content)

