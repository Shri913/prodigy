from PIL import Image

def encrypt_image(input_image_path, output_image_path, shift_value):
    # Open the input image
    img = Image.open(input_image_path)
    encrypted_img = img.copy()
    
    # Get image data
    pixels = encrypted_img.load()
    
    # Encrypt image by shifting pixel values
    for i in range(encrypted_img.size[0]):    # For every pixel in width
        for j in range(encrypted_img.size[1]): # For every pixel in height
            pixel = pixels[i, j]
            if len(pixel) == 3:  # RGB image
                r, g, b = pixel
                pixels[i, j] = ((r + shift_value) % 256,
                                (g + shift_value) % 256,
                                (b + shift_value) % 256)
            elif len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                pixels[i, j] = ((r + shift_value) % 256,
                                (g + shift_value) % 256,
                                (b + shift_value) % 256,
                                a)  # Alpha value remains the same
    
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, shift_value):
    # Open the encrypted image
    img = Image.open(input_image_path)
    decrypted_img = img.copy()
    
    # Get image data
    pixels = decrypted_img.load()
    
    # Decrypt image by reversing the shift operation
    for i in range(decrypted_img.size[0]):    # For every pixel in width
        for j in range(decrypted_img.size[1]): # For every pixel in height
            pixel = pixels[i, j]
            if len(pixel) == 3:  # RGB image
                r, g, b = pixel
                pixels[i, j] = ((r - shift_value) % 256,
                                (g - shift_value) % 256,
                                (b - shift_value) % 256)
            elif len(pixel) == 4:  # RGBA image
                r, g, b, a = pixel
                pixels[i, j] = ((r - shift_value) % 256,
                                (g - shift_value) % 256,
                                (b - shift_value) % 256,
                                a)  # Alpha value remains the same
    
    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

def main():
    # User inputs
    input_image_path = input("Enter the path to the image to encrypt: ")
    encrypted_image_path = "encrypted_image.png"
    decrypted_image_path = "decrypted_image.png"
    shift_value = int(input("Enter the shift value for encryption/decryption: "))
    
    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, shift_value)
    
    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, shift_value)
    
    # Display the images
    original_img = Image.open(input_image_path)
    encrypted_img = Image.open(encrypted_image_path)
    decrypted_img = Image.open(decrypted_image_path)
    
    original_img.show(title="Original Image")
    encrypted_img.show(title="Encrypted Image")
    decrypted_img.show(title="Decrypted Image")

if __name__ == "__main__":
    main()
