#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import send_data

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.OUT)

# Main code goes below here
try:
    while True:

	# Detect motion via PIR Sensor
        detect = GPIO.input(4)

        if(detect):
            GPIO.output(10,GPIO.HIGH)
        else:
            GPIO.output(10,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
