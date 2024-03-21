# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:56:31 2024

@author: Algyr
"""

import FakeRPi.GPIO as GPIO
import time
import atexit
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

# light status post
@app.route('/servo_room', methods=['POST'])
def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def check_servo_status():
    servo_status = json.loads(request.data)
    servo_status_bool = servo_status['servo_status']
    print(servo_status_bool)
    
    # Set up GPIO
    servo_pin = 18  # Use any GPIO pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    # Create PWM object
    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency

    # Rotate the servo
    try:
        pwm.start(2.5)  # Initial position
        time.sleep(2)

        pwm.ChangeDutyCycle(7.5)  # Rotate to 90 degrees
        time.sleep(2)

        pwm.ChangeDutyCycle(12.5)  # Rotate to 180 degrees
        time.sleep(2)

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
    
   
    return jsonify({ 'msg': 'success.' }), 201 

# END servo status post

if __name__ == '__main__':
   app.run(port=5000)
