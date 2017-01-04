# import modules
import picamera


# create instance of the PiCamera class
camera = picamera.PiCamera()


# set camera settings
camera.vflip = True


# grab an image
camera.capture('testImage.jpg')


