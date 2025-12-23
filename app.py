# Import required libraries
from flask import Flask, request, send_file, render_template_string
from cryptography.fernet import Fernet
import os

# Initialize Flask application
app = Flask(__name__)

# Folder where encrypted files are stored
UPLOAD_FOLDER = "uploads"
KEY_FILE = "key.key"

# Load encryption key from key.key file
with open(KEY_FILE, "rb") as key_file:
    key = key_file.read()

# Create fernet object for AES encryption/decryption
cipher = Fernet(key)

# Simple HTML page
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure File Upload</title>
</head>
<body>
    <h2>Secure File Upload (AES Encryption)</h2>

    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <h3>Download File</h3>
    <form action="/download" method="get">
        <input type="text" name="filename" placeholder="filename" required>
        <button type="submit">Download</button>
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()
    encrypted = cipher.encrypt(data)

    with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as f:
        f.write(encrypted)

    return "File uploaded & encrypted successfully"

@app.route("/download")
def download():
    filename = request.args.get("filename")
    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "rb") as f:
        encrypted = f.read()

    decrypted = cipher.decrypt(encrypted)

    temp_file = "temp_" + filename
    with open(temp_file, "wb") as f:
        f.write(decrypted)

    return send_file(temp_file, as_attachment=True)

if __name__ == "__main__":

    app.run(debug=True)
