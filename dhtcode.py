# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:31:27 2024

@author: Algyr
"""

import FakeRPi.GPIO as GPIO
import adafruit_dht
import time
import atexit
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# dht status post
@app.route('/dht_room', methods=['POST'])
def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def check_dht_status():
    dht_status = json.loads(request.data)
    dht_status_bool = dht_status['dht_status']
    print(dht_status_bool)

    #setting GPIO pin 18 to output
    dht_pin = 18  # Use any GPIO pin
    dht_sensor = adafruit_dht.DHT22(dht_pin)

    while True:
        if not dht_status_bool:
            break

        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            print("Temperature: {:.1f}°C, Humidity: {}%".format(temperature, humidity))
            time.sleep(2)  # Read every 2 seconds
        except RuntimeError as e:
            print("Error reading DHT sensor: {}".format(e))

    return jsonify({ 'msg': 'success.' }), 201 

#END dht status code
if __name__ == '__main__':
    app.run(port=5000)