#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import send_data

# Setup GPIO
________________
________________
________________
________________

# Main code goes below here
try:
    while True:

	# Detect motion via PIR Sensor
        ______________
        # When PIR sensor detect motion
        if(detect == 1):
            print("Motion Detected")

            # LED On
            print("LED ON")
            _______________
            # Wait 1 second
            _______________
            # LED Off
            print("LED OFF")
            # Send data
            send_data.send("___PUT YOUR NAME HERE____")
        # Wait for further motion
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
