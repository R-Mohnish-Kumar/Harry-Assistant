from langdetect import detect, DetectorFactory
from gtts import gTTS
import os
DetectorFactory.seed = 0
text='你好'
language=detect(text)
myObj=gTTS(text=text,lang=language,slow=False)
myObj.save(language+".mp3")
os.system("mpg321 "+language+".mp3")



