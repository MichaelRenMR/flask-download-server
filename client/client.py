import requests
import errno
import os
import subprocess

# remote server upload URL
URL = 'http://127.0.0.1:5000/uploads/'  # TODO: Change me

# name of file to be downloaded
FILENAME =  'hello_server.py'  # TODO: Change me

# client directory for file to be downloaded to
LOCAL_DIR = '/home/michael/Desktop/Su22/clientserverDemo/client/downloads/'  # TODO: Change me

# command to run the file locally
COMMAND = 'python ' + LOCAL_DIR + FILENAME  # TODO: Change me

response = requests.get(URL+FILENAME)

if response.status_code == 404:
	raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), FILENAME)

with open(LOCAL_DIR + FILENAME, 'wb') as f:
	f.write(response.content)

process = subprocess.Popen(COMMAND.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print(output)


