#import RPi.GPIO as GPIO
import time
import atexit
import json
from flask import Flask
import jsonify, requests
app = Flask(__name__)

employees = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]

#########
nextEmployeeId = 4

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist'}), 404
    return jsonify(employee)

def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

def employee_is_valid(employee):
    
    return True

@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400  
    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)  
    
    return '', 201, { 'location': f'/employees/{employee["id"]}' }



## light status post
#@app.route('/lights_room', methods=['POST'])
#def cleanup():
#    GPIO.cleanup()
#
#atexit.register(cleanup)
#
#def check_light_status():
#    light_status = json.loads(request.data)
#    light_status_bool = light_status['light_status']
#    print(light_status_bool)
#    #setting GPIO pin 18 to output
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(18,GPIO.OUT)
#
#    if light_status_bool == "1":
#        # light is on
#        print('light is on')
#        GPIO.output(18,GPIO.HIGH)
#    else:
#        # ligh is off
#        print('light is off')
#        GPIO.output(18,GPIO.LOW)
#

#    return jsonify({ 'msg': 'success.' }), 201 

# END light status post

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404  
    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400  
    employee.update(updated_employee)   
    
    return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404  
    employees = [e for e in employees if e['id'] != id]
    return jsonify(employee), 200

if __name__ == '__main__':
   app.run(port=5000)
