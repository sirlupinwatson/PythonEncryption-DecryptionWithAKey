# # Encrypt and decrypt a message using a Caesar cipher with a key number!



def main():
    # Get the message to encrypt
    message = input("Enter the message to encrypt: ")
    # Get the key to use for the encryption
    key = int(input("Enter the key to use for the encryption: "))
    # Encrypt the message
    ciphertext = encrypt(message, key)
    # Print the encrypted message
    print("The encrypted message is: " + ciphertext)
    # Decrypt the message
    plaintext = decrypt(ciphertext, key)
    # Print the decrypted message
    print("The decrypted message is: " + plaintext)


def encrypt(message, key):
    # Convert the message to uppercase
    message = message.upper()
    # Create an empty string to store the encrypted message
    ciphertext = ""
    # Loop through each character in the message
    for c in message:
        # Convert the character to ASCII
        ascii = ord(c)
        # If the character is a letter
        if ascii >= 65 and ascii <= 90:
            # Add the encrypted character to the encrypted message
            ciphertext += chr((ascii - 65 + key) % 26 + 65)
        # If the character is not a letter
        else:
            # Add the character to the encrypted message
            ciphertext += c
    # Return the encrypted message
    return ciphertext


def decrypt(ciphertext, key):
    # Convert the ciphertext to uppercase
    ciphertext = ciphertext.upper()
    # Create an empty string to store the decrypted message
    plaintext = ""
    # Loop through each character in the ciphertext
    for c in ciphertext:
        # Convert the character to ASCII
        ascii = ord(c)
        # If the character is a letter
        if ascii >= 65 and ascii <= 90:
            # Add the decrypted character to the decrypted message
            plaintext += chr((ascii - 65 - key) % 26 + 65)
        # If the character is not a letter
        else:
            # Add the character to the decrypted message
            plaintext += c
    # Return the decrypted message
    return plaintext


if __name__ == "__main__":
    main()


