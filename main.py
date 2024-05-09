import base64

def encode_to_base64(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def encode_to_base32(text):
    encoded_bytes = base64.b32encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text


def main():
    input_text = input("Enter the text to encode: ")
    encoded_text = encode_to_base64(input_text)
    print("Encoded text:", encoded_text)

if __name__ == "__main__":
    main()
