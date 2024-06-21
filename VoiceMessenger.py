import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
'''
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            #return data
        except sr.UnknownValueError:
            print("Not Understand")

sptext()
'''
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',250)
    engine.say(x)
    engine.runAndWait()

#speechtx("Hello Hello Hello Hello Hello vikas  Hello vikas bolo kuch to ")

speechtx("haarea krishna haarea krishna krishna krishna haarea haarea haarea raama haarea raama raama raama haaree haaree")
