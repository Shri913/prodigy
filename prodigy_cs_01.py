def caesar_cipher_encrypt(text, shift):
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Other characters remain the same
        else:
            result += char
    
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Get user input
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

# Encrypt the message
encrypted_message = caesar_cipher_encrypt(message, shift_value)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift_value)
print(f"Decrypted message: {decrypted_message}")
