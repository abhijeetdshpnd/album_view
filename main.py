import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions import show_image

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = os.environ["BUCKET_NAME"]


@app.route("/test")
def home():
    return render_template('index.html')


@app.route("/")
def list():
    contents = show_image(BUCKET)
    return render_template('collection.html', contents=contents)


app.run(host='0.0.0.0', port=8080)
