from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("speach.mp3")

text = "Hello, I am vahid azizan ghelianchi."
text_to_speech(text)
os.system("mpg321 output.mp3")
