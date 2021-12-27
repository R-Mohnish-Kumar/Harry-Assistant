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

def tamil():
    listener = speech_recognition.Recognizer()
    talk_back = pyttsx3.init()
    voices = talk_back.getProperty('voices')
    talk_back.setProperty('voice', voices[0].id)
    talk_back.setProperty('rate', 178)
    master = "Masters"

    def speak(words):
        DetectorFactory.seed = 0
        language = detect(words)
        myObj = gTTS(text=words, lang=language, slow=False)
        myObj.save(language + ".mp3")
        os.system("mpg321 " + language + ".mp3")

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        print(hour)

        if hour >= 0 and hour < 12:
            speak("good morning" + master)

        elif hour >= 12 and hour < 15:
            speak("good afternoon" + master)

        else:
            speak("good Evening" + master)

        speak("நான் ஹாரி உங்கள் உதவியாளர், நான் உங்களுக்கு ஏதாவது உதவி செய்ய முடியுமா")

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('mohnish694@gmail.com', 'AISHUMA$5')
        server.sendmail('mohnish694@gmail.com', to, content)
        server.close()

    def get_commands():
        try:
            with speech_recognition.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source, None, 400)
                command = listener.recognize_google(voice, language='ta-in')
                command = command.lower()
                print(master + ":" + command)
        except Exception as e:
            pass
        return command

    wishMe()

    def run_harry():
        print('Initializing Harry...')
        command = get_commands()
        print(command)

        if ('நீங்க யாரு' in command):
            speak('நான் ஹாரி. மோஹ்னிஷ்குமார் மற்றும் ஹரிணி ஆகியோரால் உருவாக்கப்பட்ட மெய்நிகர் உதவியாளர்')
        elif 'நேரம்' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak("தற்பொழுது நேரம்" + time)
        elif 'வாட்ஸ்அப்' in command:
            whatsapp = command.replace('வாட்ஸ்அப் திரக்கிறேன்', '')
            speak('நா யாருக்கு அனுப்ப வேண்டும்')
            print('நா யாருக்கு அனுப்ப வேண்டும்')
            to = input()
            speak('நான் என்ன செய்தி அனுப வேண்டும்')
            print('நான் என்ன செய்தி அனுப வேண்டும்')
            content = get_commands()
            speak('உங்களுடைய' + whatsapp + 'திரக்கிறது')
            pywhatkit.sendwhatmsg('+91' + to, content, 23, 28)
        elif 'செல்லவும்' in command:
            website = command.replace('செல்லவும்', '')
            speak(website + 'க்கு செல்கிரென்')
            translator = Translator(from_lang="tamil", to_lang="english")
            translation = translator.translate(website)
            print(translation)
            url_1 = 'https://www.' + translation + '.com'
            url = url_1.replace(' ', '')
            webbrowser.open(url)

        elif 'உங்க பெயர் என்ன' in command:
            speak('என் பெயர் ஹாரி')
        elif 'ஏப்படி இருக்கீங்க' in command:
            speak('நான் நன்றாக இருக்கிறேன் கேட்டதற்கு நன்றி Masters')
        elif 'चलाओ' in command:
            song = command.replace('चलाओ', '')
            speak(song + ' உங்களுக்காக ஒரு பாடல் போடுகிறேன்')
            translator = Translator(from_lang="tamil", to_lang="english")
            translation = translator.translate(song)
            print(translation)
            pywhatkit.playonyt(translation)
        elif 'ஜோக்' in command:
            speak(pyjokes.get_joke())
        elif 'யாறு' in command:
            content = command.replace('யாறு', '')
            info = wikipedia.summary(content, 1)
            print(info)
            translator = Translator(from_lang="english", to_lang="tamil")
            translation = translator.translate(info)
            print(translation)
            speak(translation)
        elif 'என்னா' in command:
            content = command.replace('என்னா', '')
            infoData = wikipedia.summary(content, 1)
            print(infoData)
            translator = Translator(from_lang="english", to_lang="tamil")
            translation = translator.translate(infoData)
            print(translation)
            speak(translation)
        elif 'சென்ரு வருகிறேன்' in command:
            speak("சென்ரு வருகிறேன் masters")
            exit()
        elif 'அஞ்சல் அனுப்புங்கो' in command:
            try:
                speak("நான் யாருக்கு அனுப வேண்டும்")
                to = input()
                speak("நான் என்ன அனுப்ப வேண்டும்")
                content = get_commands()
                sendEmail(to, content)
                speak("மின்னஞ்சல் அனுப்பப்பட்டுள்ளது தயவு செய்து ஒரு முறை பார்க்கவும்")
            except Exception as e:
                print(e)
        elif 'நீங்கள் single ளாக  இருக்கிறீர்களா?' in command:
            speak("இல்லை நான் பிணைய இணைப்பில் உள்ளேன்")
        elif 'நீ்ங்கள் ஆணா? அல்லது பெண்ணா' in command:
            speak('நான் ஆணோ பெண்ணோ அல்ல, நான் மோஹ்னிஷ்குமார் மற்றும் ஹரிணியின் மெய்நிகர் தனிப்பட்ட உதவியாளர்')
        elif 'நீங்கள் என்ன படித்தீர்கள்' in command:
            speak("உங்களைப் போல் இல்லை masters")
        else:
            speak('மன்னிக்கவும் என்னால் புரிந்து கொள்ள முடியவில்லை தயவு செய்து திருப்பி சொல்ல முடியுமாं')

    while True:
        try:
            run_harry()
        except UnboundLocalError:
            print("No command detected! I'm quiting ")
            break