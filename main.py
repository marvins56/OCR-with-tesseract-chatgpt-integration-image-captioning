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


#
# #
# import speech_recognition as sr
# import pyttsx3
#
# # Initialize text-to-speech engine
# engine = pyttsx3.init()
#
# # Initialize speech recognizer
# r = sr.Recognizer()
#
# # Keyword to wake up the system
# wake_keyword = "hey system"
#
#
# # Define your functions here
#
# def read():
#     # Function logic here
#     pass
#
#
# def describe():
#     # Function logic here
#     pass
#
#
# def send_sms():
#     # Function logic here
#     pass
#
#
# def call():
#     # Function logic here
#     pass
#
#
# def help_call():
#     # Function logic here
#     pass
#
#
# # Define a function to execute the selected function
# def execute_function(selected_function):
#     # Call the selected function
#     selected_function()
#
#     # Prompt the user to continue or exit
#     engine.say("Do you want to perform another task?")
#     engine.runAndWait()
#
#
# # Define a function to display the menu
# def display_menu():
#     engine.say("Which task do you want to perform?")
#     engine.say("You can say: read, describe, send sms, call, or help call.")
#     engine.runAndWait()
#
#
# # Run the script in a loop
# while True:
#     try:
#         # Prompt the user to select a function
#         display_menu()
#
#         # Listen to user input
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source)
#             audio = r.listen(source)
#
#         # Use Google speech recognition to convert speech to text
#         text = r.recognize_google(audio)
#
#         # Process user input
#         if wake_keyword in text.lower():
#             # User has woken up the system
#             display_menu()
#         elif "read" in text.lower():
#             execute_function(read)
#         elif "describe" in text.lower():
#             execute_function(describe)
#         elif "send sms" in text.lower():
#             execute_function(send_sms)
#         elif "call" in text.lower():
#             execute_function(call)
#         elif "help call" in text.lower():
#             execute_function(help_call)
#         else:
#             engine.say("Sorry, I didn't understand your request. Please try again.")
#             engine.runAndWait()
#
#     except sr.UnknownValueError:
#         # Speech recognition could not understand the user
#         engine.say("Sorry, I didn't catch that. Please try again.")
#         engine.runAndWait()
#
#     except sr.RequestError:
#         # Speech recognition service failed
#         engine.say("Sorry, there was an error with the speech recognition service.")
#         engine.runAndWait()
