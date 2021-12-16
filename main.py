import speech_recognition
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import smtplib
import pyjokes
import webbrowser
from langdetect import detect, DetectorFactory
from gtts import gTTS
import os

listener =speech_recognition.Recognizer()
talk_back=pyttsx3.init()
voices=talk_back.getProperty('voices')
talk_back.setProperty('voice',voices[0].id)
talk_back.setProperty('rate',178)
master="Masters"
def speak(words):
    talk_back.say(words)
    talk_back.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + master)

    elif hour>=12 and hour<15:
        speak("good afternoon" + master)

    else:
        speak("good Evening" + master)

    speak("i am harry. Your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohnish694@gmail.com', 'AISHUMA$5')
    server.sendmail('mohnish694@gmail.com',to,content)
    server.close()

def get_commands_tamil():
    try:
        with speech_recognition.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source,None,400)
            command=listener.recognize_google(voice,language='ta-in')
            command=command.lower()
            print(master+":"+command)
    except Exception as e:
        pass
    return command

def get_commands_hindi():
    try:
        with speech_recognition.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source,None,400)
            command=listener.recognize_google(voice,language='hi-in')
            command=command.lower()
            print(master+":"+command)
    except Exception as e:
        pass
    return command

def get_commands():
    try:
        with speech_recognition.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source,None,400)
            command=listener.recognize_google(voice,language='en-in')
            command=command.lower()
            print(master+":"+command)
    except Exception as e:
        pass
    return command

wishMe()

def run_harry():
    print('Initializing Harry...')
    command=get_commands()
    print(command)

    if('who are you' in command):
        speak('I am Harry.A Virtual Assistant developed by Mohnishkumar and Harini')
    elif 'hi' in command:
        speak('hey mam')
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        speak("It's "+time+ "now.")
    elif 'whatsapp' in command:
        whatsapp=command.replace('open whatsapp','')
        speak('to whom should i send')
        print('to whom should i send')
        to=input()
        speak('what is ur message')
        print('what is ur message')
        content=get_commands()
        speak('opening'+whatsapp)
        pywhatkit.sendwhatmsg('+91'+to,content,23,28)
    elif 'open' in command:
        website=command.replace('open','')
        speak("opening"+website)
        url_1='https://www.'+website+'.com'
        url=url_1.replace(' ','')
        webbrowser.open(url)

    elif 'what is your name' in command:
        speak('My name is Harry.')
    elif 'how are you' in command:
        speak('I am fine.Thanks for asking masters.')
    elif 'play' in command:
        song=command.replace('play','')
        speak('playing '+song+'...')
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'who is' in command:
        content=command.replace('who is','')
        info=wikipedia.summary(content,1)
        print(info)
        speak(info)
    elif 'what' in command:
        content=command.replace('what','')
        infoData=wikipedia.summary(content,1)
        print(infoData)
        speak(infoData)
    elif 'search for' in command:
        content = command.replace('what', '')
        infoData = wikipedia.summary(content, 1)
        print(infoData)
        speak(infoData)
    elif 'bye' in command:
        speak("bye masters. see you later")
        exit()
    elif 'send a mail' in command:
        try:
            speak("to whom should i send")
            to = input()
            speak("what should i send")
            content = get_commands()
            sendEmail(to, content)
            speak("Email has been sent. kindly have a look")
        except Exception as e:
            print(e)
    elif 'are you single' in command:
        speak("no i am in a relationship with network connection")
    elif 'are you male or female' in command:
        speak('i am not either male or female,i am a virtual personal assistant of Mohnishkumar and Harini')
    elif 'what have you studied' in command:
        speak("not much as you masters")
    else:
        speak('sorry i cant understand.can you please say it back')


while True:
    try:
        run_harry()
    except UnboundLocalError:
        print("No command detected! I'm quiting ")
        break