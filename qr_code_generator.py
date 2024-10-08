import qrcode
from PIL import ImageColor

#Function to parse color input, with a specified default color if input is invalid
def parse_color(color_input, default_color):
    try:
        #If the input is a hex color, convert it to an RGB tuple
        if color_input.startswith('#'):
            return ImageColor.getrgb(color_input)
        #If the input is an RGB tuple (e.g., "(255, 255, 255)"), evaluate it
        else:
            return eval(color_input)
    except:
        #If the input is invalid, print a message and return the default color
        print(f"Invalid color format. Using default color ({'black' if default_color == (0, 0, 0) else 'white'}).")
        return default_color  
    
#Function to create a QR code with customizable colors and save it as a JPG file
def create_qr_code(data, filename, fill_color, back_color):
    #Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )
    
    #Add the data (e.g., URL) to the QR code
    qr.add_data(data)
    qr.make(fit=True)  #Fit the QR code to the data provided
    
    #Parse the fill and background colors, defaulting to black for fill and white for background
    fill = parse_color(fill_color, (0, 0, 0))  # Default to black if fill_color is invalid
    background = parse_color(back_color, (255, 255, 255))  # Default to white if back_color is invalid
    
    #Create an image of the QR code with the specified fill and background colors
    img = qr.make_image(fill_color=fill, back_color=background)
    
    #Convert the image to RGB mode to ensure it can be saved as a JPG
    img = img.convert("RGB")
    
    #Save the image as a JPG file
    img.save(f"{filename}.jpg")
    print(f"QR code saved as {filename}.jpg with QR color {fill_color} and background color {back_color}.")

#Get inputs from the user
website_url = input("Enter the website URL you want to encode into the QR code: ")
filename = input("Enter the name for the QR code file (without extension): ")
fill_color = input("Enter the QR code color (hex or RGB): ")
back_color = input("Enter the background color (hex or RGB): ")

#Generate and save the QR code with custom colors
create_qr_code(website_url, filename, fill_color, back_color)
