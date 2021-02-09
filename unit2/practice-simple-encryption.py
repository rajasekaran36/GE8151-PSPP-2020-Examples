
plain_text = input("Enter data:")
key = int(input("key:"))

def encode(plain_text,key):
    cipher_text = ''
    for i in range(len(plain_text)):
        current_char = plain_text[i]
        ascii_value_current_char = ord(current_char)
        ascii_value_current_char_enc = ascii_value_current_char + key
        current_char_enc = chr(ascii_value_current_char_enc)
        cipher_text = cipher_text + current_char_enc
    return cipher_text

print("plain text:",plain_text)
print("cipher text:",encode(plain_text,key))