# O.S.M.D (Optical-Scanning-Mathematic-Service)
 
 Created a device that can scan and solve mathematical problems using a Pi Camera and Math-Pix API to process and identify the math being scanned

 The circuit would use a Raspberry Pi, Pi Camera, Jumper wires, and LCD screen.  The code for the device is written entirely in Python it uses libraries such as OpenCV, JSON, and RPIO.GPIO

 check out my demo

https://github.com/user-attachments/assets/b875be77-e150-4153-b954-8e496d6ffd58

To get your project working on the Raspberry Pi, you’ll need to install the necessary libraries and ensure everything is set up correctly. Here are the steps to do that:

1. Installing Libraries

Python Libraries

	1.	OpenCV (cv2):
	•	OpenCV is used for image processing and camera capture.
	•	Install it using pip:
 
 pip install opencv-python-headless

 	2.	PiCamera:
	•	PiCamera is used to interface with the Raspberry Pi camera module.
	•	Install it using pip:

 pip install picamera[array]
 
 	3.	PIL (Python Imaging Library):
	•	PIL (or its fork Pillow) is used for image manipulation and drawing.
	•	Install it using pip:

 pip install Pillow 

	4.	Adafruit SSD1306 Library:
	•	This library is required to interface with the SSD1306 OLED display.
	•	Install it using pip:

 pip install Adafruit-SSD1306
 
	5.	Requests:
	•	Requests is used for making HTTP requests to the Mathpix API.
	•	Install it using pip: 
 
 pip install requests

 Hardware Setup

	6.	Raspberry Pi Setup:
	•	Make sure your Raspberry Pi is set up and connected to the internet.
	•	Ensure the camera module is connected correctly if you’re using one.

2. Project Code Integration

Now that you have installed the required libraries, integrate your project code. Here’s a summary of what the code does:

	•	It initializes the PiCamera, sets up the SSD1306 OLED display, and defines functions for using the Mathpix OCR API to extract mathematical expressions from images.
	•	Inside the main loop (for frame in Cheat_cam.capture_continuous...), it continuously captures frames from the camera, extracts text using Mathpix OCR, evaluates the mathematical expression if found, and displays the expression and solution on the SSD1306 display.
	•	Pressing the ‘Q’ key exits the loop and closes the camera.

3. Running the Project

To run your project:

	1.	Ensure Hardware Connections:
	•	Connect the Raspberry Pi camera module if you haven’t already.
	•	Connect the SSD1306 OLED display according to its documentation.
	2.	Run the Python Script:
	•	Navigate to the directory where your Python script (final.py) is located.
	•	Run the script using Python:
python osmd.py 

3.	Monitor Output:
	•	The script will start capturing frames from the camera and displaying any detected mathematical expressions and their solutions on the OLED display.
	•	Check the terminal for debugging messages and ensure there are no errors.
	4.	Exit the Script:
	•	Press the ‘Q’ key on your keyboard to exit the script and close the camera.

4. Troubleshooting

	•	Check Dependencies:
	•	Ensure all libraries are installed correctly.
	•	Verify internet connectivity on the Raspberry Pi for the Mathpix API requests.
	•	Hardware Connections:
	•	Double-check connections for the camera module and OLED display.
	•	Ensure they are securely connected and correctly configured.
	•	Debugging Output:
	•	Use print statements in your code to debug and understand what’s happening.
	•	Check for any error messages in the terminal output.
