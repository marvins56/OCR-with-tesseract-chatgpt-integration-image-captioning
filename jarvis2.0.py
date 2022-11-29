import datetime
import os
import smtplib
import time as ti
import webbrowser as we
from email.message import EmailMessage
from time import sleep

import clipboard
import psutil
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
from newsapi import NewsApiClient

password ="f"
senderemail="okmarvins@gmail.com"

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name\"{1}\" found for `Microphone(device_index={0}`)".format(
        index, name))


def inputCommand():
    # query = input()
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            query = r.recognize_google(r.listen(source), language="en-IN")
        except Exception as e:
            print(e)
            output("Say that again please...")
    return query


def output(out):
    # print(out)
    engine.say(out)
    engine.runAndWait()


user = "Rohit"
assistant = "Jarvis"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Microsoft David aka male
# engine.setProperty("voice",voices[1].id) Microsoft zira aka female
output(f"Hello this is {assistant}")


def greet():
    hour = datetime.datetime.now().hour
    if(hour >= 6) and (hour < 12):
        output(f"Good Morning {user}")
    elif(hour >= 12) and (hour < 18):
        output(f"Good afternoon {user}")
    elif(hour >= 18) and (hour < 21):
        output(f"Good Evening {user}")
    output("How may i Assist you?")


def sendEmail():
    email_list = {
        "test": "rokano2321@to200.com"
    }
    try:
        email = EmailMessage()
        output("To whom you want to send the e-mail")
        name = inputCommand().lower()
        email["To"] = email_list[name]
        output("What is the subject of your e-mail")
        email["Subject"] = inputCommand()
        email["From"] = senderemail
        output("What should i Say?")
        email.set_content(inputCommand())
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(senderemail, password)
        s.send_message(email)
        s.close()
        output("Email has Sent")
    except Exception as e:
        print(e)
        output("Unable to send the Email")


def sendWhatMsg():
    user_list = {
        "test1": "+91 95299 16394"
    }
    try:
        output("To whom you want to send the message")
        name = inputCommand().lower()
        output("What is the message")
        we.open("https://web.whatsapp.com/send?phone=" +
                user_list[name]+"&text="+inputCommand())
        sleep(6)
        pyautogui.press("enter")
        output("Message sent")
    except Exception as e:
        print(e)
        output("Unable to send the Message")


def weather():
    city = "Jaipur"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=<Your API Key>&units=metric").json()
    temp = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temprature is {format(temp2)} degree Celsius \n Weather is {format(temp)}")


def news():
    # https://newsapi.org/account
    newsapi = NewsApiClient(api_key="<Your API Key>")
    output("What topic you need the news about")
    topic = inputCommand().lower()
    data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
    newsdata = data["articles"]
    for y in newsdata:
        output(y["description"])


def idea():
    output("What is your idea?")
    data = inputCommand().title()
    output("You said me to remember this Idea: " + data)
    with open("data.txt", "a", encoding="Utf-8") as r:
        print(data, file=r)


greet()

while True:
    query = inputCommand().lower()
    if ("time" in query):
        output("Current time is " + datetime.datetime.now().strftime("%I:%M"))
    elif ("date" in query):
        output("Current date is " + str(datetime.datetime.now().day) + " " +
               str(datetime.datetime.now().month) + " " + str(datetime.datetime.now().year))
    elif ("email" in query):
        sendEmail()
    elif ("message" in query):
        sendWhatMsg()
    elif("search" in query):
        output("What you want to search")
        we.open("https://www.google.com/search?q="+inputCommand())
    elif("youtube" in query):
        output("what you want to search on YouTube?")
        pywhatkit.playonyt(inputCommand())
    elif("weather" in query):
        weather()
    elif("news" in query):
        news()
    elif("read" in query):
        output(clipboard.paste())
    elif("covid" in query):
        r = requests.get("https://coronavirus-19-api.herokuapp.com/all").json()
        output(
            f'Confirmed cases: {r["cases"]} \nDeaths: {r["deaths"]} \nRecovered {r["recovered"]}')
    elif("workspace" in query):
        output("Which workspace you want to work on?")
        os.startfile("D:\\Work Spaces\\"+inputCommand()+".code-workspace")
    elif("joke" in query):
        output(pyjokes.get_joke())
    elif("idea" in query):
        idea()
    elif("do you know" in query):
        ideas = open("data.txt", "r")
        output(f"You said me to remember these ideas: \n{ideas.read()}")
    elif("screenshot" in query):
        pyautogui.screenshot(str(ti.time()) + ".png").show()
    elif ("cpu" in query):
        output(f"Cpu is at {str(psutil.cpu_percent())}")
    elif("offline" in query):
        hour = datetime.datetime.now().hour
        if(hour >= 21) and (hour < 6):
            output(f"Good Night {user}! Have a nice sleep")
        else:
            output(f"By {user}")
        quit()