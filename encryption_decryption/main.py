import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#encrypt
def encrypt():
    plain_text = input("Enter the message to Encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index =chars.index(letter)
        cipher_text +=key[index]

    print("Original  : ",plain_text)
    print("Encrypted : ",cipher_text)

#Decrypt
def decrypt():
    cipher_text = input("Enter the message to Decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index =key.index(letter)
        plain_text +=chars[index]

    print("Encrypted : ",cipher_text)
    print("Original  : ",plain_text)

encrypt()
print()
decrypt()
