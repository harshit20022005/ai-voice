import psutil

from voice import speechtx


def battery_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    speechtx(f"the device is running on {percent}% battery power")

if __name__ == "__main__":
    battery_percentage()