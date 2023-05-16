import random


def encrypt(text,key):
    encrypt_text = ""
    for char in text:

        encrypt_char = chr(ord(char) ^ key)
        
        encrypt_text+=encrypt_char
    print("encrypted text",encrypt_text)

    return encrypt_text

def decrypt(text,key):  
    decrypt_text = ""
    for char in text:
        decrypt_char = chr(ord(char) ^ key)
        decrypt_text += decrypt_char
    print("Decrypted text",decrypt_text)
    return decrypt_text 


test_text = "This is Text"
print("original text", test_text)
key = random.randint(12,99)


encrypt_text = encrypt(test_text,key)
decrypt_text = decrypt(encrypt_text,key)