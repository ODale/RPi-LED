''' ODale Cotterell
    Raspberry GPIO - Project
    Street light system RYG (two)
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#GPIO output setup
#GPIO Street light 1
GPIO.setup(11, GPIO.OUT, initial = 0)
GPIO.setup(13, GPIO.OUT, initial = 0)
GPIO.setup(15, GPIO.OUT, initial = 0)

#GPIO Street light 2
GPIO.setup(19, GPIO.OUT, initial = 0)
GPIO.setup(21, GPIO.OUT, initial = 0)
GPIO.setup(23, GPIO.OUT, initial = 0)

try:
    counter = 1
    while True:
        GPIO.output(11, True)   #1 Green light on
        GPIO.output(23, True)   #2 Red light on
        time.sleep(4.9/10)
        GPIO.output(11, False)  #1 Green light off
        time.sleep(.1/10)
        GPIO.output(13, True)   #1 Yellow light on
        time.sleep(1.9/10)
        GPIO.output(13, False)  #1 Yellow light off
        GPIO.output(23, False)  #2 Red light off
        time.sleep(.1/10)
        GPIO.output(15, True)   #1 Red light on
        GPIO.output(19, True)   #2 Green light on
        time.sleep(4.9/10)
        GPIO.output(19,False)   #2 Green light off
        time.sleep(.1/10)
        GPIO.output(21, True)   #2 Yellow light on
        time.sleep(1.9/10)
        GPIO.output(21, False)  #2 Yellow light off
        GPIO.output(15, False)  #1 Red light off
        time.sleep(.1/10)
        counter += 1
        
except KeyboardInterrupt:
    pass

print counter

GPIO.cleanup()
