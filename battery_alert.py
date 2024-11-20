import random
import time
import psutil
from DLG import low_b, last_low, full_battery
import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound

def speechtx(text):
    tts = gTTS(text=text, lang='en')
    filename = "output.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def battery_alert():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
         
    while True:
        time.sleep(10)
       

        if percent < 30:
            random_low = random.choice(low_b)
            speechtx(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            speechtx(random_low)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speechtx(random_low)
        else:
            pass
        time.sleep(1500)

def battery_alert1():
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speechtx(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            speechtx(random_low)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speechtx(random_low)
        else:
            speechtx("sir,your battery is in perfect battery level")


