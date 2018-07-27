#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import send_data

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.OUT)
# Initiate a counter
i = 0

# Main code goes below here
try:
    while True:

        # Print a counter
        print(i)

	# Detect motion via PIR Sensor
        detect = GPIO.input(4)

        # When PIR sensor detect motion
        if(detect):
            print("Motion Detected")

            print("LED ON")
            GPIO.output(10,GPIO.HIGH)

            # Send data to server
            send_data.send("PutYourNameHere")

            # Wait a moment
            time.sleep(10)

            print("LED OFF")
            GPIO.output(10,GPIO.LOW)

            i = 0

        # Wait a little before detecting further motion
        time.sleep(1)
        # Increase a counter
        i += 1

except Exception:
    GPIO.cleanup()
