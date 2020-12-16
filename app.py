from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

import os

UPLOAD_FOLDER = os.path.abspath("./uploads/")
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge"])

def allowed_file(filename):

    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():

    return "Architectural style recnigtion"

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if not "file" in request.files:
            return "No file part in the form."
        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("get_file", filename=filename))
        return "File not allowed."

    return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Select image</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <style type="text/css">
    h1 {padding: 40px;text-align:left; background:#420021; color:white; font-size:35px}
    </style>
</head>
<body>
    <h1>Select image</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>"""

@app.route("/uploads/<filename>")
def get_file(filename):

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)