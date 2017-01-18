"""
Moition Sensor First Test
01/18/2017
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# GPIO pin number initialized as input
pinN = 7
GPIO.setup(pinN, GPIO.IN)


try:
    while True:
        
        moSen = GPIO.input(pinN)

        if moSen == 1:
            if flag == 0:
                print "Motion Detected!"
                flag = 1
        else:
            flag = 0

except KeyboardInterrupt:
    print "Exiting..."
    pass

    
GPIO.cleanup()
