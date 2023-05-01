import os
import speech_recognition as sr

from CompleteModels.reuse import capture_image, speak
from Read_from_Image import process_image
from chatBot import process_user_input
from imageCaption import CaptionImage


def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1  # Increase the pause threshold

    with sr.Microphone() as source:
        speak("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Add a delay before listening
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        speak(f"Recognized: {text}")
        return text.lower()
    except:
        speak("Sorry, I could not understand that.")
        return ""


def myAssistant():
    while True:
        text = recognize_speech()

        if "read text" in text:
            path = capture_image()
            if path and os.path.exists(path):
                # process the image using the process_image() function
                process_image(path)
            else:
                speak("Error: Could not capture image or path is invalid.")

        elif "my sorrounding" in text:
            path = capture_image()
            CaptionImage(path)

        elif "function three" in text:
            process_user_input()

        elif "exit" in text:
            speak("closing program......have a nice day")
            break


myAssistant()
