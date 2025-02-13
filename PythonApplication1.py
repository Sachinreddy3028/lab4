from flask import Flask , request
import boto3
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

# Initialize Flask app
app = Flask(_name_)

# AWS S3 Configuration
S3_BUCKET = "your-secure-bucket"
s3_client = boto3.client('s3')

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
if file:
    s3_client.upload_fileobj(file, S3_BUCKET, file.filename,ExtraArgs={"ServerSideEncryption": "AES256"})
            return {"message": "File uploaded securely."}, 200
    return {"error": "No file provided."}, 400

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
