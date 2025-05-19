import base64
from Crypto.Cipher import AES

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt(message, key):
    key = key[:16].ljust(16, '0').encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(encrypted_message, key):
    key = key[:16].ljust(16, '0').encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted.decode('utf-8').rstrip()
