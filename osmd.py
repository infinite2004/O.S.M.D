import time
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image, ImageDraw, ImageFont
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import requests
import json

# Set your Mathpix API key
mathpix_api_key = ''

# Function to extract text using Mathpix OCR
def mathpix_ocr(image):
    url = "https://api.mathpix.com/v3/text"
    headers = {
        "app_id": mathpix_api_key,
        "app_key": mathpix_api_key,
    }

    # Convert the image to PNG format
    _, img_encoded = cv2.imencode(".png", image)
    
    # Create a file-like object from the image data
    img_file = {"file": ("image.png", img_encoded.tobytes(), "image/png")}
    
    # Specify desired options in JSON format
    options_json = {
        "formats": ["text", "data", "html"],
        "data_options": {
            "include_svg": True,
            "include_table_html": True,
            "include_latex": True,
            "include_tsv": True,
            "include_asciimath": True,
            "include_mathml": True,
        },
        "confidence_threshold": 0.8,  # Set your desired confidence threshold
    }

    # Send a POST request with image and options
    response = requests.post(url, headers=headers, files=img_file, data={"options_json": json.dumps(options_json)})

    try:
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        print("API Response:", result)  # Print the entire API response

        # Check if the 'text' key is present in the result
        if 'text' in result:
            return result["text"]
        else:
            print("Error: 'text' key not found in Mathpix OCR response")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error in Mathpix OCR request: {e}")
        return ""

# Raspberry Pi pin configuration:
RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize PiCamera
Cheat_cam = PiCamera()
Cheat_cam.resolution = (640, 480)
Cheat_cam.framerate = 60
Cheat_cam.rotation = 0
Cheat_cam.sharpness = 50
rawCapture = PiRGBArray(Cheat_cam, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

# Initialize the LCD display
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Enter the loop after PiCamera is initialized
for frame in Cheat_cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image_np = frame.array

    # Clear the LCD screen
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Use Mathpix OCR to extract text from the image
    text = mathpix_ocr(image_np)

    # Display the solution or "*" on the LCD screen
    try:
        if text:
            result = eval(''.join(char for char in text if char.isdigit() or char in '+-*/'))
            print("Math Expression:", text)
            print("Solution:", result)

            # Display the mathematical expression on the LCD screen
            text_width, text_height = draw.textsize(text, font)
            x = (width - text_width) // 2
            y = (height - text_height) // 2
            draw.text((x, y), text, font=font, fill=255)

            # Display the solution on the LCD screen
            solution_text = f"Solution: {result}"
            text_width, text_height = draw.textsize(solution_text, font)
            y += text_height + 5
            draw.text((x, y), solution_text, font=font, fill=255)
        else:
            draw.text((x, y), "*", font=font, fill=255)

        # Update the LCD screen
        disp.image(image)
        disp.display()

    except Exception as e:
        print(f"Error evaluating expression: {e}")

    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)

    # Check for the 'Q' key to exit the loop and close the PiCamera
    if key == ord("Q"):
        break

# Release the resources
Cheat_cam.close()
cv2.destroyAllWindows()
disp.clear()
disp.display()
