# import os
import pyttsx3  # converts text to speech
import openai
from CompleteModels.reuse import speak
# get API key from top-right dropdown on OpenAI website
openai.api_key = "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"

def complete(prompt):
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

    return speak(res['choices'][0]['text'].strip())

speak("processing query")
query = (
    "how to create a luganda chatbot"
)

complete(query)


