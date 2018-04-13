# --- imports ---

from google.cloud import storage
import six
import sys
import os
import datetime
from random import randint
from PIL import Image

# --- Globals ---
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./rpi-fp-cred.json"
PROJECT_ID = 'rpi-fp'
CLOUD_STORAGE_BUCKET = 'rpi-fp-123'
MAX_CONTENT_LENGTH = 8*1024*1024 # Enter the maximum size of your image file
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


### Check file extension
def _check_extension(filename, allowed_extensions):
    if ('.' not in filename or
            filename.split('.').pop().lower() not in allowed_extensions):
    	return -1
    else: return 0

### Generate a new filename
def _safe_filename(filename):
    #filename = secure_filename(filename)
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    basename, extension = filename.rsplit('.', 1)
    return "{0}-{1}.{2}".format(basename, date, extension)

### Upload image
def upload_file(file_stream, filename, content_type):
	if _check_extension(filename, ALLOWED_EXTENSIONS):
		print('ok')
	else:
		print('Not ok')
	filename = _safe_filename(filename)

	client = storage.Client().from_service_account_json('./rpi-fp-cred.json')
	bucket = client.bucket(CLOUD_STORAGE_BUCKET)
	blob = bucket.blob(filename)
	blob.upload_from_string(file_stream, content_type=content_type)
	url = blob.public_url
	if isinstance(url, six.binary_type):
		url = url.decode('utf-8')
	return url

### Capture image and start the process
### ----
import picamera
with picamera.PiCamera() as camera:
    camera.resolution=(1024,1024)
    new_image= 'image-'+str(randint(0,100))+'.jpg'
    camera.capture(new_image)
### ----

### Local file as image 
# new_image = 'image-59.jpg'
### ----

local_file = new_image
with open(local_file) as f:
	im = f.read()
	print(im[0:33])
print (upload_file(im, local_file, 'image/jpeg'))
print (upload_file(im, local_file, 'image/jpeg'))
