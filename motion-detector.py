#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import send_data

# Setup GPIO
------------------------
------------------------
------------------------
------------------------
# Initiate a counter
i = 0

# Main code goes below here
try:
    while True:

        # Print a counter
        print(i)

	# Detect motion via PIR Sensor
        __________________________

        # When PIR sensor detect motion
        if(detect):
            print("Motion Detected")

            print("LED ON")
            _________________________

            # Send data to server
            send_data.send("PUT YOUR NAME HERE")

            # Wait a moment
            time.sleep(3)

            print("LED OFF")
            _________________________

        # Wait a little before detecting further motion
        time.sleep(0.5)
        # Increase a counter
        i += 1

except KeyboardInterrupt:
    GPIO.cleanup()
