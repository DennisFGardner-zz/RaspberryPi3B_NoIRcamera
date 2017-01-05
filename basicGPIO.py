import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

print 'holding'

time.sleep(20)

print 'done'

GPIO.cleanup()
