from gtts import gTTS
import os
myText='நலமா'
language='ta'
myObj=gTTS(text=myText,lang=language,slow=False)
myObj.save("tamil.mp3")
os.system("mpg321 tamil.mp3")