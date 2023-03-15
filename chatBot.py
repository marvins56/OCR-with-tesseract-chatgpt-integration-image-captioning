import openai
import speech_recognition as sr
import pyttsx3
from CompleteModels.reuse import *
# Initialize OpenAI API
openai.api_key = "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"

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
    speak(feedback)


# Keyword to stop the conversation
stop_keyword = "stop"
back_keyword = "menu"

while True:
    wishMe()
    # Prompt user for input using text-to-speech

    # Use speech recognition to convert user's speech to text
    speech_to_text()
    text_generated = speech_to_text()
    # Convert user input to lowercase for easier keyword matching
    user_input = text_generated.lower()

    # Check if user input contains the stop keyword
    if stop_keyword in user_input:
        speak(" STOP keyword detected")
        speak("stopping system")
        break
    elif back_keyword in user_input:
        speak(" menu keyword detected")


    # Get feedback from OpenAI GPT API
    speak("processing input,..... Kindly hold on..")
    get_feedback_from_chat_gpt(user_input)
    speak("processing complete .")


