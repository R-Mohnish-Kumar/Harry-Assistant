from translate import Translator
translator = Translator(from_lang="hindi",to_lang="english")
translation = translator.translate("फ्लिपकार्ट")
print(translation)