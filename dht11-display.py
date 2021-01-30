import adafruit_dht
import time
#import RPi.GPIO as GPIO
import board
import json
import datetime

pin = board.D4

#GPIO.setup(pin, GPIO.IN)

dht_device = adafruit_dht.DHT11(pin)

while True:
    humidity = dht_device.humidity
    temperature = dht_device.temperature

    reading = json.dumps({'humidity': humidity, 'temperature': temperature, 'datetime': datetime.utcnow()})

    print(reading, sort_keys=True, indent=4)

    time.sleep(3);
