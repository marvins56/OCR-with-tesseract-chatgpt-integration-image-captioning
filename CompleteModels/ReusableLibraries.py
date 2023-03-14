import pyttsx3
import datetime
import cv2
import pytesseract

import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail

import os
# Connects pytesseract(wrapper) to the trained tesseract module
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # hour = datetime.datetime.now().hour
    if(hour >= 6) and (hour < 12):
        speak(f"Good Morning ")
    elif(hour >= 12) and (hour < 18):
        speak(f"Good afternoon ")
    elif(hour >= 18) and (hour < 21):
        speak(f"Good Evening ")

        speak("How may i Assist you?")


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
