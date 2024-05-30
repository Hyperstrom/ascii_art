from PIL import Image
import numpy as np

def stretch_image(input_image_path):
    """Open the original image and stretch its width."""
    with Image.open(input_image_path) as img:
        original_width, original_height = img.size
        # Calculate new dimensions
        new_width = int(original_width * 2.35)
        new_height = original_height  # Height remains the same
        # Resize the image
        stretched_img = img.resize((new_width, new_height), Image.LANCZOS)
        return stretched_img

def convert_image_to_ascii(image_path, GCF=1.0, width=400):
    # Stretch the image
    img = stretch_image(image_path)

    # Resize the image while maintaining the aspect ratio
    aspect_ratio = img.width / img.height
    new_width = width
    new_height = int(new_width / aspect_ratio)
    img = img.resize((new_width, new_height))

    # Convert the image to grayscale
    img = img.convert('L')

    # Convert the image to a numpy array
    img = np.asarray(img)

    # Normalize the pixel values to range from 0 to 1
    img = img / 255.0

    # Apply gamma correction
    img = img ** GCF

    # Define the ASCII characters for the art
    chars = np.asarray(list(' .,:;rt='))

    # Map the grayscale values to ASCII characters
    ascii_img = chars[(img * (chars.size - 1)).astype(int)]

    # Create a string representation of the ASCII art
    ascii_str = '\n'.join([''.join(row) for row in ascii_img])

    # Save the ASCII art to a text file
    with open('ascii_art.txt', 'w') as f:
        f.write(ascii_str)
    
    return ascii_str

# Example usage
image_path = 'selfie.png'  #paste your one image path
ascii_art = convert_image_to_ascii(image_path)
print(ascii_art)
