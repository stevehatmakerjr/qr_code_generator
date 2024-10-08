# QR Code Generator with Custom Colors (Python)
This Python project allows you to generate QR codes with customizable colors for both the QR code itself and its background. Users can input their desired colors in either hex or RGB formats. The program ensures that default colors (black for the QR code and white for the background) are used if invalid inputs are provided. It saves the generated QR codes as JPG files.

Features:
Generates QR codes from URLs or text
Customizable QR code color and background color
Supports hex and RGB color formats
Saves QR codes as JPG files
Default colors for invalid inputs (black for QR code, white for background)

Technologies Used:
Python
qrcode library
Pillow (PIL) for image handling

How to Use:
Clone the repository.
Install required dependencies using pip install qrcode[pil].
Run the script and follow the prompts to input a URL, filename, and colors.
The QR code will be generated and saved as a JPG file.
