import cv2
import numpy as np
from PIL import Image, ImageTk

# Image loading function
def load_image(path):
    img = cv2.imread(path)
    return img

# Show OpenCV image on a Tkinter label
def show_image_on_label(img, label):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=im_pil)
    label.imgtk = imgtk
    label.configure(image=imgtk)

# Encode secret message into image
def encode_message(img, secret_message):
    # Convert message to binary with delimiter '1111111111111110' (16 bits)
    binary_message = ''.join([format(ord(i), '08b') for i in secret_message])
    binary_message += '1111111111111110'  # delimiter to mark end of message

    data_index = 0
    total_bits = img.shape[0] * img.shape[1] * 3  # total bits available

    if len(binary_message) > total_bits:
        raise ValueError("Message too long to encode in image.")

    encoded_img = img.copy()
    rows, cols, _ = encoded_img.shape

    for row in range(rows):
        for col in range(cols):
            for channel in range(3):  # B, G, R channels
                if data_index < len(binary_message):
                    pixel_val = encoded_img[row, col, channel]
                    # Clear least significant bit and set to message bit
                    new_val = (int(pixel_val) & ~1) | int(binary_message[data_index])
                    encoded_img[row, col, channel] = np.uint8(new_val)
                    data_index += 1
                else:
                    return encoded_img  # Encoding complete

    return encoded_img


# Decode secret message from image
def decode_message(img):
    binary_data = ''
    flat_img = img.flatten()

    for i in range(len(flat_img)):
        binary_data += str(flat_img[i] & 1)

    # Split binary string into bytes of 8 bits
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    message = ''
    i = 0
    while i < len(all_bytes):
        byte = all_bytes[i]
        # Check for delimiter start
        if byte == '11111111':
            # Check next two bytes for full delimiter sequence
            if i + 2 < len(all_bytes):
                if all_bytes[i+1] == '11111111' and all_bytes[i+2] == '11111110':
                    break  # Found delimiter, stop decoding
        try:
            message += chr(int(byte, 2))
        except:
            break  # Invalid byte, stop decoding
        i += 1

    return message
