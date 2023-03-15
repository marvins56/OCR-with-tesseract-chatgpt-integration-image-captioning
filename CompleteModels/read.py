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
from reuse import *
import os
# Connects pytesseract(wrapper) to the trained tesseract module
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def process_image(image_path):

    # Read image file
    img = cv2.imread(image_path)
    hImg, wImg, none = img.shape
    box = pytesseract.image_to_boxes(img)
    data = pytesseract.image_to_data(img)


    # Initialize variables
    string = ''

    speak("Image selected...., processing image")
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

    speak("Image processing complete.. Results are:")
    # Use pyttsx3 to read the text
    speak(string)

    speak("There you go, End of result.")
    # Save the audio file
    speak("File saving initialized,")

    engine.save_to_file(string, filedir + '/audio.mp3')
    speak("File saved successfully.")


    # # Output the bounding box with the image
    # cv2.imshow('Image output', image_path)
    # cv2.waitKey(0)



capture_image()

path = capture_image()

path = capture_image()

if path and os.path.exists(path):
    # process the image using the process_image() function
    process_image(path)
else:
    speak("Error: Could not capture image or path is invalid.")




