import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from voice import *



def get_internet_speed():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_driver_path = r'/DATA/chromedriver.exe'

        service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get('https://fast.com/')
        speechtx("Checking your Internet speed")
        time.sleep(11)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'speed-value')))

        speed_element = driver.find_element(By.ID, 'speed-value')

        speed_value = speed_element.text

        return speed_value
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if driver:
            driver.quit()

def check_internet_speed():
    speed_result = get_internet_speed()

    if speed_result is not None:
        speak(f"Sir, your internet speed is: {speed_result} Mbps")
    else:
        speak("Error: Unable to retrieve internet speed.")

