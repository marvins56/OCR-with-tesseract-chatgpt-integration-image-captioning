import a as a
import cv2
import pytesseract
import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail

import os
# Connects pytesseract(wrapper) to the trained tesseract module
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'




# capture image
def capture_image():
    cap = cv2.VideoCapture(0) # Open the default camera
    if not cap.isOpened():
        return None
    ret, frame = cap.read() # Capture a frame
    cap.release() # Release the camera
    if not ret:
        return None
    return frame



def process_image(image_path):

    # Read image file
    img = cv2.imread(image_path)
    hImg, wImg, none = img.shape
    box = pytesseract.image_to_boxes(img)
    data = pytesseract.image_to_data(img)

    # Initialize pyttsx3
    engine = pyttsx3.init()

    # Set properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Decrease the rate by 50

    # Initialize variables
    string = ''

    engine.say("Image selected...., processing image")
    engine.runAndWait()
    # Create directory to store files
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S")
    filedir = './files/' + filename
    if not os.path.exists(filedir):
        os.makedirs(filedir)

    # Open the file with write permission
    filewrite = open(filedir + '/string.txt', "w")

    # Process each line in the data string
    for z, a in enumerate(data.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) >= 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # Display detected word under each bounding box
                cv2.putText(img, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
                # Append the detected word to the string
                string += a[11] + " "
                # Writing to the file
                filewrite.write(a[11] + " ")

    filewrite.close()

    # Save the string to a text file
    with open(filedir + '/string.txt', 'w') as file:
        file.write(string)

    engine.say("Image processing complete.. Results are:")
    # Use pyttsx3 to read the text
    engine.say(string)
    engine.runAndWait()
    engine.say("There you go, End of result.")
    # Save the audio file
    engine.say("File saving initialized,")

    engine.save_to_file(string, filedir + '/audio.mp3')
    engine.say("File saved successfully.")
    engine.runAndWait()

    # Output the bounding box with the image
    # cv2.imshow('Image output', img)
    # cv2.waitKey(0)


# process_image("../words.PNG")
#
# def capture_image():
#     # Initialize the camera
#     camera = cv2.VideoCapture(0)
#     if not camera.isOpened():
#         print("Could not open camera")
#         return None
#
#     # Capture a frame from the camera
#     ret, frame = camera.read()
#     if not ret:
#         print("Could not capture frame")
#         camera.release()
#         return None
#
#     # Get the current date and time for filename
#     now = datetime.datetime.now()
#     timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
#
#     # Create directory if it doesn't exist
#     dir_name = "images"
#     if not os.path.exists(dir_name):
#         os.makedirs(dir_name)
#
#     # Save the image to file
#     file_path = os.path.join(dir_name, f"{timestamp}.jpg")
#     cv2.imwrite(file_path, frame)
#
#     # Release the camera
#     camera.release()
#
#     # Return the file path
#     return file_path
def capture_image():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    # Wait for user to press a key to take image
    while True:
        ret, frame = cap.read()
        cv2.imshow('Press Space to Capture Image', frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Get current date and time
            now = datetime.datetime.now()
            filename = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Create directory if it does not exist
            directory = './images/'
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Save image
            filepath = os.path.join(directory, f"{filename}.png")
            cv2.imwrite(filepath, frame)

            # Release camera and close window
            cap.release()
            cv2.destroyAllWindows()

            return filepath


path = capture_image()

path = capture_image()

if path and os.path.exists(path):
    # process the image using the process_image() function
    process_image(path)
else:
    print("Error: Could not capture image or path is invalid.")




