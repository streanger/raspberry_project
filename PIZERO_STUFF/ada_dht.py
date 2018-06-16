#!/usr/bin/python
import sys
import Adafruit_DHT
from time import sleep
import datetime
from gpiozero import LED

greenLED = LED(24)

def dht_read():
    now = datetime.datetime.now()
    measureTime = ":".join(str(x) for x in [now.hour, now.minute, now.second])
    humidity, temperature = Adafruit_DHT.read_retry(11, 23) #read vs read_retry
    if humidity is not None and temperature is not None:
        print("Hum: %s, Temp: %s, T: %s" % (humidity, temperature, measureTime))
    else:
        print "--< read failed"

while (1):
    sleep(60)
    greenLED.on()
    try:
        dht_read()
    except:
        pass
        print("--< failed")
    greenLED.off()


'''
zapisywac temperature w pliku csv; staly czas, zapisujemy wylacznie kolejne wskazania temperatury i oddzielnie wilgotnosci
'''
