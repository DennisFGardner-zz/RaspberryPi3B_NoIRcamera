#!/usr/bin/env python
""" MAIN.py
This program takes images using the NoIR camera on a Raspberry Pi 3 B. 
"""

# import modules
import picamera
import datetime
from time import sleep


def main():
    # PARAMETERS

    # number of images
    N = 3600/2

    # delay between images (seconds)
    delay = 2
    
    # create instance of the PiCamera class
    camera = picamera.PiCamera()
    
    # set camera settings (I want to read about these more and optimize for low light)
    camera.vflip = True
    camera.brightness = 50 # not sure if this is before or after the capture,
    # I have not heard of a brightness adjustment before on a caera


    for ii in range(0,N):

        # timestamp w/ second accuracy 
        timeStr = getTimeStamp()

        # grab an image
        camera.capture('images/'+timeStr+'.jpg')
        
        sleep(delay)
        
        print float(ii+1)/N * 100



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



















    
