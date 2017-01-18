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


for ii in range(0,1000):

##    print ii

    moSen = GPIO.input(pinN)

    print moSen


    
GPIO.cleanup()
