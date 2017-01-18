"""
Testing a break from a while loop
01/18/2017
"""

from time import sleep

try:
    while True:
        print "Everthing is good!"
        sleep(1)

except KeyboardInterrupt:
    print "Exiting..."
    pass

