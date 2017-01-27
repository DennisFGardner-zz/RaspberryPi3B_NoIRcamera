#!/usr/bin/env python
""" MAIN.py
This program takes images using the NoIR camera on a Raspberry Pi 3 B.

Last update: 01/27/2017
"""

# import modules
import picamera
import datetime
from time import sleep
import RPi.GPIO as GPIO


def main():
    
    # initialize parameters
    pinN = 7
    flag = 0
    delay = 1 # time between images

    # initialize board
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinN, GPIO.IN)

    # create instance of the PiCamera class
    camera = picamera.PiCamera()
    
    # set camera settings (I want to read about these more and optimize for low light)
    camera.vflip = True

    print "System On" 

    try:
        while True:

            moSen = GPIO.input(pinN)

            if moSen == 1:
                if flag == 0:
                    
                    # timestamp w/ second accuracy 
                    timeStr = getTimeStamp()
                    
                    print "Motion Detected at %s" % timeStr
                    
                    # grab an image
                    camera.capture('images/'+timeStr+'.jpg')
                    
                    flag = 1
                    
                    sleep(delay)

            else:
                flag = 0

    except KeyboardInterrupt:
        print "Exiting..."
        pass

    print "cleaning up"
    GPIO.cleanup()


def getTimeStamp():
    """
    This function gets a timestamp in the following format:
    Year    Month     Day      _ 24Hour   Min      Sec
    4 digits 2 digits 2 digits _ 2 digits 2 digits 2 digits
    """
    
    now =datetime.datetime.now()

    timeStr = now.strftime('%Y%m%d_%H%M%S')
    
    #print('Time Stamp (Year Month Day _ 24H min sec): '+timeStr)
    
    return timeStr


if __name__ == "__main__":
    main()

print "System Off"















    
