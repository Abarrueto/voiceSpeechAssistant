import speech_recognition as sr
import pyttsx3
import pywhatkit
from spotify2py import Spotify

# Spotify Token option
token2 = ""

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
name = 'siri'

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='en-EN')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)

    except:
        pass
    return rec

# Options to do
# TODO:  "HOF and just call one function"
def run():
    rec = listen()
    if 'play' in rec:
        music = rec.replace('play', '')
        talk('Playing' + music)
        pywhatkit.playonyt(music)




run()
