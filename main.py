import speech_recognition as sr
import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the available actions
actions = ["read", "chat", "play music"]

# Define a function to perform an action based on the user's input
def perform_action(action):
    if action == "read":
        # Perform the read action
        print("Reading...")
    elif action == "chat":
        # Perform the chat action
        print("Chatting...")
    elif action == "play music":
        # Perform the play music action
        print("Playing music...")

# Define a function to listen for voice commands
def listen_for_commands():
    # Initialize the speech recognition engine
    r = sr.Recognizer()

    while True:
        # Listen for voice input
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)

        # Attempt to recognize the voice command
        try:
            command = r.recognize_google(audio).lower()
            print("Command: " + command)

            # Check if the command is one of the available actions
            if command in actions:
                # Perform the action
                perform_action(command)

                # Prompt the user for the next action
                engine.say("What would you like to do next?")
                engine.runAndWait()
            else:
                # Unrecognized command
                engine.say("Sorry, I didn't understand that. Please try again.")
                engine.runAndWait()

        # Handle any errors with the speech recognition engine
        except sr.UnknownValueError:
            engine.say("Sorry, I didn't catch that. Please try again.")
            engine.runAndWait()
        except sr.RequestError as e:
            engine.say("Sorry, I'm having trouble with my speech recognition. Please try again later.")
            engine.runAndWait()

        # Hibernation after 1 minute of inactivity
        time.sleep(60)

# Start listening for voice commands
listen_for_commands()
