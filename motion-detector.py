#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import send_data

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(_____, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(_____), GPIO.OUT)
# Initiate a counter
i = 0

# Main code goes below here
try:
    while True:

        # Print a counter
        print(i)

	# Detect motion via PIR Sensor
        --------------------------------

        # When PIR sensor detect motion
        if(detect):
            print("Motion Detected")

            print("LED ON")
            --------------------------------

            # Send data to server
            send_data.send("PutYourNameHere")

            # Wait a moment
            time.sleep(10)

            print("LED OFF")
            --------------------------------

            i = 0

        # Wait a little before detecting further motion
        time.sleep(1)
        # Increase a counter
        i += 1

except Exception:
    GPIO.cleanup()
