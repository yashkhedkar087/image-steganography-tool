
# 🕵️‍♂️ Image Steganography Tool with Encryption (Python + Tkinter + OpenCV)

A secure image steganography desktop application built using Python, Tkinter, and OpenCV. This tool allows users to **hide secret messages** inside images using **LSB (Least Significant Bit)** technique, and **encrypts** the message using **Fernet symmetric encryption** before embedding. Users can also decode and decrypt hidden messages from images.



## 📌 Features

- 📂 Load and preview images
- 🔒 AES-level encryption using `cryptography.fernet`
- 🖼️ Embed hidden messages inside image pixels (LSB technique)
- 🔍 Decode and decrypt secret messages from images
- 💻 User-friendly GUI using Tkinter
- 🧠 Secure from plain-text detection
- 🧹 Delimiter-based message termination to prevent junk data



## 📁 Folder Structure


image-steganography/
│
├── main.py                  # Main GUI application
├── encryption.py            # Contains encrypt and decrypt functions
├── utils.py                 # Utility functions for image processing and steganography
├── README.md                # Project documentation
└── requirements.txt         # Required Python packages


## ✅ Requirements

Install all required packages with:


pip install -r requirements.txt

**requirements.txt**

opencv-python
numpy
pillow
pycryptodome
base64

## 🚀 How to Run

1. **Clone the repository**:

 
   git clone https://github.com/your-username/image-steganography.git
   cd image-steganography
   

2. **Install dependencies**:

 
   pip install -r requirements.txt
   

3. **Run the app**:


   python main.py
   


## 🛠️ Usage Guide

### ▶️ Encode & Save Image
1. Click **"Load Image"** and select a PNG/JPG image.
2. Enter the **secret message** and **encryption key**.
3. Click **"Encode & Save Image"** — select path to save encoded image.

### 🔓 Decode Message
1. Enter the **correct encryption key**.
2. Click **"Load Image & Decode Message"**.
3. Decrypted hidden message will be shown if key is correct.



## 🔐 Encryption Details

This app uses **Fernet (AES 128 CBC + HMAC)** encryption from the `cryptography` package. The message is encrypted before embedding and decrypted after decoding.



## 📷 Steganography Technique

- The Least Significant Bit (LSB) of each pixel is modified to hide encrypted message bits.
- A delimiter `#####` is used to mark the end of the hidden message.



## ⚠️ Limitations

- Works best with lossless image formats like `.png` and `.bmp`.
- Avoid using very large messages on small images.
- Wrong encryption key will result in failure to decrypt message.



## 💡 Future Enhancements

- Drag-and-drop support for images
- Support for hiding text files or other data
- Password-based key derivation using `PBKDF2`
- Dark mode UI
- Support for hiding in audio or video files



## 👨‍💻 Author

**Yash Khedkar**  
Cybersecurity Enthusiast | Python Developer | MCA Graduate  
🌐 [LinkedIn](https://www.linkedin.com/in/yash-khedkar1907/)


## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

