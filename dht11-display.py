import adafruit_dht
import time
import RPi.GPIO as GPIO
import json
import datetime

pin = 4

GPIO.setup(pin, GPIO.IN)

dht_device = adafruit_dht.DHT11(GPIO.input(pin))

while True:
    humidity = dht_device.humidity
    temperature = dht_device.temperature

    reading = json.dumps({'humidity': humidity, 'temperature': temperature, 'datetime', datetime.utcnow()})

    print(reading, sort_keys=True, indent=4)
    #if humidity is not None and temperature is not None:
    #    print("Temp=(0:0.1f)C Humidity=(1:0.1f)%".format(temperature, humidity))
    #else:
    #    print("Sensor failure. Check wiring.")

    time.sleep(3);
