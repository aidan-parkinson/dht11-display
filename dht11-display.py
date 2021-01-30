import adafruit_dht
import time
import Rpi.GPIO as GPIO

setup = GPIO.setup(4, GPIO.IN)

dht_device = adafruit_dht.DHT11(GPIO.input(setup))

while True:
    humidity, temperature = (dht_device.humidity, dht_device.temperature)
    if humidity is not None and temperature is not None:
        print("Temp=(0:0.1f)C Humidity=(1:0.1f)%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(3);
