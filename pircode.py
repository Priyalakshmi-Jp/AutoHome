# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:51:18 2024

@author: Algyr
"""

import FakeRPi.GPIO as GPIO
import time
import atexit
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

# pir status post
@app.route('/pir_room', methods=['POST'])
def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def check_pir_status():
    pir_status = json.loads(request.data)
    pir_status_bool = pir_status['pir_status']
    print(pir_status_bool)
    
   # Set up GPIO
    pir_pin = 18  # Use any GPIO pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_pin, GPIO.IN)
 
    if pir_status_bool:
        if GPIO.input(pir_pin) == GPIO.HIGH:
            print("Motion detected!")
        else:
            print("No motion detected.")

    GPIO.cleanup()


    return jsonify({ 'msg': 'success.' }), 201 

# END pir status post

if __name__ == '__main__':
   app.run(port=5000)
