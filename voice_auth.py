import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha


# The voice Id can be set as either 0 or 1,

# 0 indicates Male voice

# 1 indicates Female voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language = 'en-in')
        
        except:
            speak("pardon me, please say that again")
            return "None"
        return statement
    
speak("Loading your AI personal assistant Citroēn")
