# Connection between Google Cloud Storage (GCP) and Raspberry Pi 3B

## Target
- Raspberry Pi is most commonly used device in IoT Platform 
- Efficient analytics on data captured from Raspberry Pi is transferred to Server running in GCP or Amazon EC2.
- We use Google cloud storage functions help in transfer of data to Google cloud platform.

---
## Packages Required
- Python 3.7 (Preferably above by the time you read this!)
- Google cloud storage.
- PIL (For Image Transformations)
- picamera (For capturing images in Raspberry Pi)


## Procedure
### Credentials Required for Authentication.
- Login to [Google cloud platform](https://console.cloud.google.com)
- Create a new Bucket and give it a name (Preferably a project that you are working on)
- Create a Key for Authentication [credentials](https://console.cloud.google.com/apis/credentials)
- Create a JSON Key and download it to your project folder.
- For reference [GCP_Python_Documentation](https://cloud.google.com/storage/docs/reference/libraries)
---
### Functions
- Global Name Spaces are declared such as
 - PROJECT_ID,CLOUD_STORAGE_BUCKET,ALLOWED_EXTENSIONS
- _ _check_extension_ so that only specific files are uploaded (Helpful in Security)
- _ _safe_filename_ to embed the file name with the capture date and time.
- upload_file to upload the file to the cloud storage.
