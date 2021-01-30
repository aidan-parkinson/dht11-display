import adafruit_dht
import time
import RPi.GPIO as GPIO

pin = 4

GPIO.setup(pin, GPIO.IN)

dht_device = adafruit_dht.DHT11(GPIO.input(pin))

while True:
    humidity, temperature = (dht_device.humidity, dht_device.temperature)
    if humidity is not None and temperature is not None:
        print("Temp=(0:0.1f)C Humidity=(1:0.1f)%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(3);
