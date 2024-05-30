# 📸🎨 Image to ASCII Art Converter 📄✨

Welcome to the **Image to ASCII Art Converter**! This Python script transforms any image into an ASCII art text file, making your pictures look super cool in text format. Just input your image path, and voila! You'll get a stylish ASCII art representation. 🎉

## Features 🌟
- **Simple to Use**: Just paste the image path in the code, and it does the rest.
- **Customizable Width**: Converts images to a fixed width of 400 characters for consistency.
- **Text File Output**: Generates an easy-to-share `.txt` file containing your ASCII art.

## Prerequisites 🛠️
- Python 3.10
- Pillow library for image processing

You can install Pillow using pip:
```sh
pip install pillow
```

## How to Use 🚀

1. **Clone the Repository** 📂
   ```sh
   git clone https://github.com/Hyperstrom/ascii_art.git
   cd <your-repo-folder>
   ```

2. **Run the Script** 🖥️
   ```sh
   python ascii_art.py
   ```

3. **Provide Image Path** 🖼️
   Paste the path of the image you want to convert in the script:
   ```python
   image_path = 'path/to/your/image.jpg'
   ```

4. **Get Your ASCII Art** 🎨
   Check the output directory for the generated `.txt` file. Open it, and enjoy your ASCII masterpiece! 📄✨

## How It Works 🔍

### Step 1: Image Opening and Resizing 📏
The script starts by opening the image you provide. It resizes the image to a fixed width of 400 pixels while maintaining the aspect ratio. This ensures the ASCII art maintains the proportions of the original image.

### Step 2: Grayscale Conversion 🌑
The image is then converted to grayscale. This step simplifies the image by reducing it to shades of gray, making it easier to map pixel values to ASCII characters.

### Step 3: Pixel to ASCII Mapping 🅰️
The script uses a predefined set of ASCII characters that represent different levels of brightness: `'.,:;rt='`. Each pixel's brightness is mapped to an appropriate ASCII character. Darker pixels might be represented by characters like 'r' or 't', while lighter pixels might be represented by '.' or ','.

### Step 4: Formatting the ASCII Art 🖼️
The ASCII characters are assembled into a string that matches the dimensions of the resized image. The string is then formatted to ensure it wraps correctly to the specified width, creating the final ASCII art.

### Step 5: Saving the Output 💾
Finally, the ASCII art string is saved into a text file. You can open this file with any text editor to view and share your ASCII art.

## Example 🖼️➡️📄
This is some example of ASCII Art Conversion from image 

![photo_2024-05-30_11-18-11](https://github.com/Hyperstrom/ascii_art/assets/112319058/64bcece8-d418-433b-9a85-01f3819fd789)

![photo_2024-05-30_11-18-03](https://github.com/Hyperstrom/ascii_art/assets/112319058/e12cc87a-1000-492f-9604-83b8fd47193f)


## Contributions 🤝
Feel free to fork this repository, make improvements, and submit pull requests. Let's make this tool even better together! 

Enjoy creating awesome ASCII art! 🎉🖼️📄✨

---

*Made with 💖 by Aniket Pal*
