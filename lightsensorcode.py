# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:41:27 2024

@author: Algyr
"""

import FakeRPi.GPIO as GPIO
import time
import atexit
import json
import board
import busio
import adafruit_tsl2591
from flask import Flask, jsonify, request

app = Flask(__name__)

# lightsensor status post
@app.route('/lightsensor_room', methods=['POST'])
def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def check_lightsensor_status():
    lightsensor_status = json.loads(lightsensor_status)
    lightsensor_status_bool = lightsensor_status['lightsensor_status']
    print(lightsensor_status_bool)

    # Set up I2C
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the sensor object
    sensor = adafruit_tsl2591.TSL2591(i2c)

    # Read light levels
    if lightsensor_status_bool:
        print("Lux: {}".format(sensor.lux))
        time.sleep(2)  # Read every 2 seconds
    else:
        print("Light sensor reading is off")

    return jsonify({ 'msg': 'success.' }), 201 

# END lightsensor status post

if __name__ == '__main__':
    app.run(port=5000)