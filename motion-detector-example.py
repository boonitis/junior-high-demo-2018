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

        # When PIR sensor detect motion
        if(detect == 1):
            print("Motion Detected")
            # Blink LED
            GPIO.output(10,GPIO.HIGH)
            print("LED ON")
            # Wait 1 second
            time.sleep(1)
            GPIO.output(10,GPIO.LOW)
            print("LED OFF")
            # Send data to server
            send_data.send("BOON")
        # Wait for further motion
        time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()
