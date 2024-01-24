import importlib.util
import lib.util.find_spec 'RPi.GPIO'
import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """

import FakeRPi.GPIO as GPIO
import time
import atexit
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

# light status post
@app.route('/lights_room', methods=['POST'])
def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

def check_light_status():
    light_status = json.loads(request.data)
    light_status_bool = light_status['light_status']
    print(light_status_bool)
    #setting GPIO pin 18 to output
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)

    if light_status_bool == "1":
        # light is on
        print('light is on')
        GPIO.output(18,GPIO.HIGH)
    else:
        # ligh is off
        print('light is off')
        GPIO.output(18,GPIO.LOW)


    return jsonify({ 'msg': 'success.' }), 201 

# END light status post

if __name__ == '__main__':
   app.run(port=5000)
