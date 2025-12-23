# FUTURE_CS_03
# Secure File Upload System with AES Encryption

## Project Overview
This project is a secure web-based file upload and download system developed using Python Flask.
All uploaded files are encrypted using AES encryption before being stored on the server and
are decrypted only during download.

This project demonstrates secure file handling concepts used in cybersecurity.

---

## Technologies Used
- Python
- Flask
- AES Encryption (Fernet - symmetric encryption)
- HTML (basic UI)

---

## How Security Is Implemented

### AES Encryption
- AES symmetric encryption is used to protect files at rest.
- When a user uploads a file, it is encrypted before saving.
- Stored files appear unreadable (encrypted format).
- During download, the file is decrypted and delivered in its original form.

### Encryption Key Management
- The file key.key stores the AES encryption key.
- This key is generated once and reused for encryption and decryption.
- In real-world applications, this key should be stored securely (environment variables or key vault).

### File Encryption at Rest
- Files stored inside the uploads/ folder are encrypted.
- Opening uploaded files directly from the folder shows unreadable data.
- This confirms encryption at rest.

---

## Features
- Secure file upload
- Secure file download
- AES encryption for stored files
- Simple and user-friendly interface
- Demonstration of secure file handling

---

## How to Run the Project
1. Install required packages:
pip install flask cryptography

2. Run the application:
python app.py

3. Open browser and visit:
http://127.0.0.1:5000

---

## Security Notes
- This project is for learning purposes.
- Proper authentication and key storage should be added in production systems.
