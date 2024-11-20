import threading
from voice import *



def jarvis():
    t2 = threading.Thread(target=battery_alert)
    t3 = threading.Thread(target=check_plugin_status)
    t2.start()
    t3.start()
    t2.join()
    t3.join()
   


jarvis()