import openai
import speech_recognition as sr
import pyttsx3
import secrets

import apiKey
from CompleteModels.reuse import *

# Initialize OpenAI API
openai.api_key = secrets.api_key

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# function to process text
def get_feedback_from_chat_gpt(prompt):
    # query text-davinci-003
    res = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Convert feedback text to speech using text-to-speech engine
    feedback = res['choices'][0]['text'].strip()
    # SAVE FEEDBACK
    save_and_speak_feedback(prompt, feedback)


def save_and_speak_feedback(prompt, feedback):
    # save conversation to file
    folder_name = "conversations"
    date_now = datetime.datetime.now().strftime('%Y-%m-%d')
    file_name = f"{date_now}.txt"

    # check if folder exists, create it if not
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # open file, append conversation with timestamp
    with open(os.path.join(folder_name, file_name), 'a') as f:
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        f.write(timestamp + " User: " + prompt + "\n")
        f.write(timestamp + " AI: " + feedback + "\n")

    # speak feedback
    speak("preparing  results....")
    speak(feedback)

while True:
    wishMe()
    # Prompt user for input using text-to-speech

    # Use speech recognition to convert user's speech to text
    # speech_to_text()
    text_generated = speech_to_text()
    # Convert user input to lowercase for easier keyword matching
    user_input = text_generated.lower()

    # Get feedback from OpenAI GPT API
    speak("processing input,..... Kindly hold on..")
    get_feedback_from_chat_gpt(user_input)
    speak("processing complete .")
