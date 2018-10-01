# Connection between Google Cloud Storage and Raspberry Pi 3B

## Target
- Raspberry pi is most commonly used device in IoT Platform 
- To do efficient Analytics on Data that is captured from Raspberry pi we transfer the data to high capability Server.
- Google Cloud Storage functions help in transfer of data.

---
## Packages Required
- Python 3.7 (Preferably above by the time you read this!)
- Google cloud Storage.
- PIL (For Image Transformations)
- picamera ( For capturing Images in Raspberry pi)


## Procedure
### Credentials Required for Authentication.
- Create a Google account and proceed to [Google-Storage](https://console.cloud.google.com)
- Create a new Bucket and give it a name (Preferably a project you are working on)
- Create a Key for Authentication [Key](https://console.cloud.google.com/apis/credentials)
- Create a JSON Key and download it to your project folder.
- For reference [GCP_Python_Documentation](https://cloud.google.com/storage/docs/reference/libraries)
---
### Functions used
- Global Name Spaces are declared such as
 - PROJECT_ID,CLOUD_STORAGE_BUCKET,ALLOWED_EXTENSIONS
- _ _check_extension_ so that only specific files are uploaded (Helpful in Security)
- _ _safe_filename_ to embed the file name with the capture date and time.
- upload_file to upload the file to the cloud storage.
