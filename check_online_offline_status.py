import requests 
from speak import *


def is_online(url="http://www.google.com", timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code >= 200 and response.status_code < 300
    except requests.ConnectionError:
        return False

def internet_status():
    if is_online():
        x = "YES SIR ! I AM READY AND ONLINE"
        speak(x)
    else:
        x = "HEY THERE SIR ! I AM FRIDAY , SORRY BUT JARVIS IS CURRENTLY NOT ONLINE"
        print(x)
