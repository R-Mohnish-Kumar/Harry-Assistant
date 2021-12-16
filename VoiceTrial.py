from langdetect import detect, DetectorFactory
from gtts import gTTS
import os
DetectorFactory.seed = 0
text='नमस्ते मास्टर्स'
language=detect(text)
myObj=gTTS(text=text,lang=language,slow=False)
myObj.save(language+".mp3")
os.system("mpg321 "+language+".mp3")



