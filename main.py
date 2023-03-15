#
# import os
# import speech_recognition as sr
# from CompleteModels.read import process_image
# from CompleteModels.reuse import capture_image, speak, wishMe, speech_to_text
# from chatBot import get_feedback_from_chat_gpt
# from imageCaption import CaptionImage
#
# r = sr.Recognizer()
#
# # Keyword to wake up the system
# wake_keyword = "hey"
#
# def read():
#     capture_image()
#     path = capture_image()
#     if path and os.path.exists(path):
#         # process the image using the process_image() function
#         process_image(path)
#     else:
#         speak("Error: Could not capture image or path is invalid.")
#     pass
#
#
# def describe():
#     capture_image()
#     path = capture_image()
#     CaptionImage(path)
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
# def AskQuestion():
#     # # Function logic here
#     # # speech_to_text()
#     # text_generated = speech_to_text()
#     #
#     # speak("processing input,..... Kindly hold on..")
#     # get_feedback_from_chat_gpt(text_generated)
#     # speak("processing complete .")
#     pass
#
#
# def execute_function(selected_function):
#     # Call the selected function
#     selected_function()
#
#     # Prompt the user to continue or exit
#     speak("Do you want to perform another task?")
#
# # Define a function to display the menu
# def display_menu():
#     speak("Which task do you want to perform?")
#     speak("You can say: read, describe, send sms, call,help call, or question to process command.")
#
# # Run the script in a loop
# while True:
#     try:
#         wishMe()
#         # Prompt the user to select a function
#         display_menu()
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
#             speak("Yes please, Am always with you.. how may i help you")
#             wishMe()
#             display_menu()
#
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
#         elif "question" in text.lower():
#             execute_function(AskQuestion)
#         else:
#             speak("Sorry, I didn't understand your request. Please try again.")
#
#
#     except sr.UnknownValueError:
#         # Speech recognition could not understand the user
#         speak("Sorry, I didn't catch that. Please try again.")
#
#     except sr.RequestError:
#         # Speech recognition service failed
#         speak("Sorry, there was an error with the speech recognition service.")
#
