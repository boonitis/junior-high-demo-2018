#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

# Setup GPIO

# Main code goes below here
try:
    while True:

	# Detect motion via PIR Sensor

        # When PIR sensor detect motion
        if(detect == 1):
            print("Motion Detected")

            # LED On
            print("LED ON")

            # Wait 1 second

            # LED Off
            print("LED OFF")

        # Wait for further motion
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
