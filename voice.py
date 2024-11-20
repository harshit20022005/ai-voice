import pyjokes
import speech_recognition as sr
import webbrowser
import datetime
import objc
from gtts import gTTS
from playsound import playsound
import os
import random
import time
import psutil
from battery_alert import *
from check_battery_persentage import *
from battery_plug_check import *
from caption_in_video import *
from play_music_in_youtube import *
from search_in_youtube import *

def speechtx(text):
    tts = gTTS(text=text, lang='en')
    filename = "output.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognising...")
            query=recognizer.recognize_google(audio)
            print(f"User said:{query}\n")
        except Exception as e:
            print(e)
            print("Sorry, I did not catch that. Please repeat.")
            return "None"
        return query.lower()

if __name__ == "__main__":
    speechtx("Hello,I am Sophia, How can I help you")

    while True:
        command = sptext().lower()

        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speechtx(f"The time is {current_time}")

        elif 'open browser' in command:
            speechtx("Opening web browser")
            webbrowser.open('http://www.google.com')

        elif 'play music' in command:
            speechtx("Playing music")
            os.system("open -a Music")
        
        elif 'battery percentage' in command:
            battery_percentage()

        elif 'battery alert' in command:
            battery_alert1()

        elif 'battery status' in command:
            check_plugin_status1()

        elif 'volume up' in command:
            volume_up()

        elif 'volume down' in command:
            volume_down()

        elif 'play on YouTube' in command:
            play_music_on_youtube()

        elif 'shutdown' in command:
            speechtx("Goodbye!")
            break

        else:
            speechtx("Sorry, I didn't understand that command.")

