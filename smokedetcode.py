# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:15 2024

@author: Algyr
"""

import FakeRPi.GPIO as GPIO
import time
import atexit
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

# smokedet status post
@app.route('/smokedet_room', methods=['POST'])
def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def check_smokedet_status():
    smokedet_status = json.loads(request.data)
    smokedet_status_bool = light_status['smokedet_status']
    print(smokedet_status_bool)
    
    # Set up GPIO
    smoke_pin = 18  # Use any GPIO pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(smoke_pin, GPIO.IN)
    
    # Check for smoke detection
    if smokedet_status_bool:
        if GPIO.input(smoke_pin) == GPIO.HIGH:
            print("Smoke detected!")
        else:
            print("No smoke detected.")

    return jsonify({ 'msg': 'success.' }), 201 

# END smokedet status post

if __name__ == '__main__':
   app.run(port=5000)
