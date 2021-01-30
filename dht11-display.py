import adafruit_dht
import time
import board
import json
from datetime import datetime

pin = board.D4

dht_device = adafruit_dht.DHT11(pin)

while True:
    humidity = dht_device.humidity
    temperature = dht_device.temperature

    reading = json.dumps({'humidity': humidity, 'temperature': temperature, 'datetime': datetime.now()}, sort_keys=True, indent=4, default=str)

    print(reading)

    time.sleep(3);
