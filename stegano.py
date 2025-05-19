def encode_message(img, secret_message):
    binary_message = ''.join([format(ord(i), '08b') for i in secret_message])
    binary_message += '1111111111111110'  # delimiter

    data_index = 0
    total_pixels = img.shape[0] * img.shape[1] * 3

    if len(binary_message) > total_pixels:
        raise ValueError("Message too long to encode in image.")

    flat_img = img.flatten()

    for i in range(len(flat_img)):
        if data_index < len(binary_message):
            flat_img[i] = (flat_img[i] & ~1) | int(binary_message[data_index])
            data_index += 1
        else:
            break

    encoded_img = flat_img.reshape(img.shape)
    return encoded_img


def decode_message(img):
    binary_data = ''
    flat_img = img.flatten()

    for i in range(len(flat_img)):
        binary_data += str(flat_img[i] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    message = ''
    for byte in all_bytes:
        if byte == '11111111':
            next_bits = ''.join(all_bytes[all_bytes.index(byte)+1:all_bytes.index(byte)+3])
            if next_bits == '1111111111111110':
                break
        message += chr(int(byte, 2))

    return message
