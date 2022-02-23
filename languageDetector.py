from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0
print(detect('நீங்கள் எப்படி இருக்கிறீர்கள்'))