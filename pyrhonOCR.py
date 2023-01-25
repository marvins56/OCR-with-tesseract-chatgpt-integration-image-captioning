import a as a
import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail


# Connects pytesseract(wrapper) to the trained tesseract module
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# engine = pyttsx3.init(
#     'sapi5')  # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
# voices = engine.getProperty('voices')  # gets you the details of the current voices
# engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice
#
#
# def speak(audio):  # function for assistant to speak
#     engine.say(audio)
#     engine.runAndWait()  # without this command, the assistant won't be audible to us
#
#
# def wishme():  # function to wish the user according to the daytime
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak('Good Morning')
#
#     elif hour > 12 and hour < 18:
#         speak('Good Afternoon')
#
#     else:
#         speak('Good Evening')
#
#     speak('Hello, I am See, your personal  assistant. how may I help you')
#
#
# def takecommand():  # function to take an audio input from the user
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         r.pause_threshold = 2
#         audio = r.listen(source)
#
#     try:  # error handling
#         speak('A moment, processing...')
#         query = r.recognize_google(audio, language='en-in')
#         # using google for voice recognition
#         print(f'User said: {query}\n')
#
#     except Exception as e:
#         speak('sorry, i did not get that, Say that again please...')  # 'say that again' will be printed in case of improper voice
#         return 'None'
#     return query
#
#
# def sendemail(to, content):  # function to send email
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('senders_eamil@gmail.com', 'senders_password')
#     server.sendmail('senders_email@gmail.com', to, content)
#     server.close()
#
#
# if __name__ == '__main__':  # execution control
#     wishme()
#     while True:
#         query = takecommand().lower()
#
#         # converts user asked query into lower case
#
#         # The whole logic for execution of tasks based on user asked query
#
#         if '' in query:
#             speak("Initialising camera")
#             # speak('Searching Wikipedia....')
#             # query = query.replace('wikipedia', '')
#             # results = wikipedia.summary(query, sentences=5)
#             # print(results)
#             # speak(results)
#
#         elif 'open youtube' in query:
#             webbrowser.open('youtube.com')
#
#         elif 'open google' in query:
#             webbrowser.open('google.com')
#
#         elif 'play music' in query:
#             speak('okay boss')
#             music_dir = 'F:\\kauta marvin\\gospel'
#             songs = os.listdir(music_dir)
#             os.startfile(os.path.join(music_dir, songs[0]))
#
#
#         elif 'time' in query:
#             strtime = datetime.datetime.now().strftime('%H:%M:%S')
#             speak(f'Sir the time is {strtime}')
#
#         elif 'open stack overflow' in query:
#             webbrowser.open('stackoverflow.com')
#
#         elif 'open free code camp' in query:
#             webbrowser.open('freecodecamp.org')
#
#         elif 'pycharm' in query:
#             codepath = 'pycharm_directory_of_your_computer'
#             os.startfile(codepath)
#
#         elif 'email' in query:
#             try:
#                 speak('what should i write in the email?')
#                 content = takecommand()
#                 to = 'reciever_email@gmail.com'
#                 sendemail(to, content)
#                 speak('email has been sent')
#             except Exception as e:
#                 print(e)
#                 speak('Sorry, I am not able to send this email')
#
#         elif 'exit' in query:
#             speak('okay boss, please call me when you need me')
#             quit()



# # connecting live video stream
# video = cv2.VideoCapture("rtsp://172.20.10.11/1"
video = cv2.VideoCapture(1)


# Setting width and height for video feed
video.set(3, 640)
video.set(4, 500)

# Allows continuous frames
while True:
    # Capture each frame from the video feed
    ret, frame = video.read()
    data = pytesseract.image_to_data(frame)
    for z, a in enumerate(data.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data1' string into a list stored in 'a'
            a = a.split()
            # Checking if array contains a word
            if len(a) >= 12:
                # Storing values in the right variables
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # Display detected word under each bounding box
                cv2.putText(frame, a[11], (x + 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
# Output the bounding box with the image
    cv2.imshow('Video output', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        break

# Image feeds
img1 = cv2.imread('Capture_1.JPG')
img2 = cv2.imread('Capture_2.JPG')
img3 = cv2.imread('Capture_3.JPG')
img4 = cv2.imread('img4.png')
img5 = cv2.imread('img.png')


# # Obtains only the string from images without visual feedback
# print(pytesseract.image_to_string(img1))
# print(pytesseract.image_to_string(img2))
# print(pytesseract.image_to_string(img3))

# Obtain the height and width for each image 3rd value is not needed
# ONLY FOR CHARACTER
h1Img, w1Img, none1 = img1.shape
h2Img, w2Img, none2 = img2.shape
h3Img, w3Img, none3 = img3.shape
h4Img, w4Img, none4 = img4.shape



# cv2.waitKey(0)
# GETTING BUNDING BOXES
# Convert images into bounding box values: x, y, width and height
# ONLY FOR CHARACTERS
box1 = pytesseract.image_to_boxes(img1)
box2 = pytesseract.image_to_boxes(img2)
box3 = pytesseract.image_to_boxes(img3)
box4 = pytesseract.image_to_boxes(img4)
box5 = pytesseract.image_to_boxes(img5)



# Convert images into bound data values: level, page no, block no, paragraph no,
# line no, word no, x, y, width, height, conf, value
# ONLY FOR WORDS

data1 = pytesseract.image_to_data(img1)
data2 = pytesseract.image_to_data(img2)
data3 = pytesseract.image_to_data(img3)
data4 = pytesseract.image_to_data(img4)
data5 = pytesseract.image_to_data(img5)
#
# for z, a in enumerate(data1.splitlines()):
#     if z!= 0:
#         a=a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w,h = int(a[8]),int(a[9])
#             cv2.rectangle(img1,(x,y),(x+w , y+h),(255,0,0),1)
#             # Display detected word under each bounding box
#             cv2.putText(img1, a[11], (x,y + 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
# for z, a in enumerate(data2.splitlines()):
#     if z!= 0:
#         a=a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w,h = int(a[8]),int(a[9])
#             cv2.rectangle(img2,(x,y),(x+w , y+h),(255,0,0),1)
#             cv2.putText(img2, a[11], (x,y + 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
#
# for z, a in enumerate(data3.splitlines()):
#     if z!= 0:
#         a=a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w,h = int(a[8]),int(a[9])
#             cv2.rectangle(img3,(x,y),(x+w , y+h),(255,0,0),1)
#             cv2.putText(img3, a[11], (x,y + 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
#
# cv2.imshow('image 1', img1)
# cv2.imshow('image 2', img2)
#
# cv2.imshow('image 3', img3)
#
# cv2.waitKey(0)

# # doing the same for all boxes
# #above code convets image to list of values and then accessed inseparate cvalues using the splict funvtion
# for a in box1.splitlines():
#     # allows access of values as an array
#     a = a.split()
#     # print(a)
# #     like ['T', '488', '349', '501', '367', '0']
# #        t is actual text detected next is x cordinte , y cordinate, width and height
# #     store thevalues in variables
# # conversion from string to int
#
#     x,y = int(a[1]),int(a[2])
#     w,h = int(a[3]),int(a[4])
#     # to place binding boxes on the same line we subtract the hight and with of the images
#     cv2.rectangle(img1,(x,h1Img-y),(w,h1Img - h),(255,0,0),1)
# #     Displaying words being detected
#     cv2.putText(img1, a[0], (x, h1Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
# #     image , with and height font, dont size colour
#
#
# for a in box2.splitlines():
#     a = a.split()
#     x,y = int(a[1]),int(a[2])
#     w,h = int(a[3]),int(a[4])
#     cv2.rectangle(img2,(x,h2Img-y),(w,h2Img - h),(255,0,0),1)
#     cv2.putText(img2, a[0], (x, h2Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
#
# for a in box3.splitlines():
#     a = a.split()
#     x,y = int(a[1]),int(a[2])
#     w,h = int(a[3]),int(a[4])
#     # to place binding boxes on the same line we subtract the hight and with of the images
#     cv2.rectangle(img3,(x,h3Img-y),(w,h3Img - h),(255,0,0),1)
#     cv2.putText(img3, a[0], (x, h3Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
# #     DIAPLAY ALL IMAGES
# cv2.imshow('image 1', img1)
# cv2.imshow('image 2', img2)
# cv2.imshow('image 3', img3)
#
# cv2.waitKey(0)

# TTS
# Open the file with write permission
filewrite = open("String.txt", "w")
for z, a in enumerate(data5.splitlines()):
    # Counter
    if z != 0:
        # Converts 'data1' string into a list stored in 'a'
        a = a.split()
        # Checking if array contains a word
        if len(a) >= 12:
            # Storing values in the right variables
            x, y = int(a[6]), int(a[7])
            w, h = int(a[8]), int(a[9])
            # Display bounding box of each word
            cv2.rectangle(img5, (x, y), (x + w, y + h), (0, 0, 255), 1)
            # Display detected word under each bounding box
            cv2.putText(img5, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
            # Writing to the file
            filewrite.write(a[11] + " ")
filewrite.close()
# Open the file with read permission
fileread = open("String.txt", "r")
language = 'en'
line = fileread.read()
if line != " ":
    fileread.close()
    speech = gTTS(text=line, lang=language, slow=False)
    speech.save("audio.mp3")
# Output the bounding box with the image before audio file
cv2.imshow('Image output', img5)
cv2.waitKey(0)
playsound("audio.mp3")

