import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

#Set Rate
engine.setProperty('rate', 190)

#Set Volume
engine.setProperty('volume', 1.0)

#Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if (hour>=6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour>=12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour>=16) and (hour < 24):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. What do you need boy")

def take_user_input():
    """Takes user input, reocgnizes it using Speech Recognition module and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Go on, say something champ...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-KE')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night boy, don't forget to check under the bed for monsters")
            else:
                speak('Do not the door hit you where the Good Lord split you')
            exit()
    except Exception:
        speak('Come again?')
        query = 'None'
    return query