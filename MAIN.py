# import modules
import picamera
import datetime


now =datetime.datetime.now()

timeStr = now.strftime('%Y%m%d_%H%M%S')
print('Time Stamp (Year Month Day _ 24H min sec): '+timeStr)


# create instance of the PiCamera class
camera = picamera.PiCamera()


# set camera settings (I want to read about these more and optimize for low light)
camera.vflip = True
camera.brightness = 50 # not sure if this is before or after the capture,
# I have not heard of a brightness adjustment before on a caera

# grab an image
camera.capture('images/'+timeStr+'.jpg')


