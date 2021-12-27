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
from translate import Translator

listener =speech_recognition.Recognizer()
talk_back=pyttsx3.init()
voices=talk_back.getProperty('voices')
talk_back.setProperty('voice',voices[0].id)
talk_back.setProperty('rate',178)
master="Masters"
def speak(words):
    DetectorFactory.seed = 0
    language = detect(words)
    myObj = gTTS(text=words, lang=language, slow=False)
    myObj.save(language + ".mp3")
    os.system("mpg321 " + language + ".mp3")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + master)

    elif hour>=12 and hour<15:
        speak("good afternoon" + master)

    else:
        speak("good Evening" + master)

    speak("मैं हैरी हूँ आपका सहायक क्या मेरे द्वारा आपकी कोई सहायता हो सकती है")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohnish694@gmail.com', 'AISHUMA$5')
    server.sendmail('mohnish694@gmail.com',to,content)
    server.close()

def get_commands():
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

wishMe()

def run_harry():
    print('Initializing Harry...')
    command=get_commands()
    print(command)

    if('कौन हो तुम' in command):
        speak('मैं हैरी हूं। मोहनीशकुमार और हरिनी द्वारा विकसित एक आभासी सहायक')
    elif 'टाइम' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        speak(time+ "बज रहा है")
    elif 'व्हाट्सएप्प' in command:
        whatsapp=command.replace('व्हाट्सएप्प चालू करो','')
        speak('मुझे किसे भेजना चाहिए')
        print('मुझे किसे भेजना चाहिए')
        to=input()
        speak('आपका संदेश क्या है')
        print('आपका संदेश क्या है')
        content=get_commands()
        speak('आपका'+whatsapp+'चालू कर रहा हूं')
        pywhatkit.sendwhatmsg('+91'+to,content,23,28)
    elif 'खोलो' in command:
        website=command.replace('खोलो','')
        speak(website+'चालू कर रहा हूं')
        translator = Translator(from_lang="hindi",to_lang="english")
        translation = translator.translate(website)
        print(translation)
        url_1='https://www.'+translation+'.com'
        url=url_1.replace(' ','')
        webbrowser.open(url)

    elif 'तुम्हारा नाम क्या है' in command:
        speak('मेरा नाम हैरी है')
    elif 'कैसे हो' in command:
        speak('मैं ठीक हूँ पूछने के लिए धन्यवाद Masters')
    elif 'चलाओ' in command:
        song=command.replace('चलाओ','')
        speak(song+' चला रहा हुं')
        translator = Translator(from_lang="hindi", to_lang="english")
        translation = translator.translate(song)
        print(translation)
        pywhatkit.playonyt(translation)
    elif 'जोक' in command:
        speak(pyjokes.get_joke())
    elif 'कौन है' in command:
        content=command.replace('कौन है','')
        info=wikipedia.summary(content,1)
        print(info)
        translator = Translator(from_lang="english", to_lang="hindi")
        translation = translator.translate(info)
        print(translation)
        speak(translation)
    elif 'क्या' in command:
        content=command.replace('क्या','')
        infoData=wikipedia.summary(content,1)
        print(infoData)
        translator = Translator(from_lang="english", to_lang="hindi")
        translation = translator.translate(infoData)
        print(translation)
        speak(translation)
    elif 'बाई' in command:
        speak("बाई masters. जल्द मिलते हैं")
        exit()
    elif 'मेल भजो' in command:
        try:
            speak("मुझे किसे भेजना चाहिए")
            to = input()
            speak("मुझे क्या भेजना चाहिए")
            content = get_commands()
            sendEmail(to, content)
            speak("ईमेल भेजा जा चुका है। कृपया एक नज़र डालें")
        except Exception as e:
            print(e)
    elif 'क्या आप single हैं' in command:
        speak("नहीं मैं नेटवर्क कनेक्शन के साथ संबंध में हूं")
    elif 'आप पुरुष हैं या महिला' in command:
        speak('मैं या तो पुरुष या महिला नहीं हूं, मैं मोहनीशकुमार और हरिणी का आभासी निजी सहायक हूं')
    elif 'बेहतर क्या' in command:
        speak("आप जितना नहीं masters")
    else:
        speak('क्षमा करें मैं समझ नहीं पा रहा हूं क्या आप कृपया इसे वापस कह सकते हैं')


while True:
    try:
        run_harry()
    except UnboundLocalError:
        print("No command detected! I'm quiting ")
        break