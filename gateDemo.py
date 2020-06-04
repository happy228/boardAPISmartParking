from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

app = Flask('openGate')

@app.route('/')
def index():
    return'u r now in gate_opener. To open gate send /open_gate'

@app.route('/open_gate')
def open_gate():
    GPIO.output(21, GPIO.HIGH)
    return 'opened'
@app.route('/close_gate')
def close_gate():
    GPIO.output(21, GPIO.LOW)
    return 'closed'

app.run(debug=True, port=3000, host='192.168.0.100')
