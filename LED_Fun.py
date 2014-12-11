''' ODale Cotterell
    Raspberry GPIO - Project
    
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#GPIO output setup
GPIO.setup(11, GPIO.OUT, initial = 0)
GPIO.setup(13, GPIO.OUT, initial = 0)
GPIO.setup(15, GPIO.OUT, initial = 0)
GPIO.setup(19, GPIO.OUT, initial = 0)
GPIO.setup(21, GPIO.OUT, initial = 0)
GPIO.setup(23, GPIO.OUT, initial = 0)

try:
    counter = 1
    #main loop
    while True:
        GPIO.output(11, True)   
        time.sleep(.1)
        GPIO.output(11, False)
        time.sleep(.1)
        GPIO.output(13, True)
        time.sleep(.1)
        GPIO.output(13, False)
        time.sleep(.1)
        GPIO.output(15, True)
        time.sleep(.1)
        GPIO.output(15, False)
        #mixup
        if (counter%2 == 0):
            GPIO.output(19, True)   
            time.sleep(.1)
            GPIO.output(19, False)
            time.sleep(.1)
            GPIO.output(21, True)
            time.sleep(.1)
            GPIO.output(21, False)
            time.sleep(.1)
            GPIO.output(23, True)
            time.sleep(.1)
            GPIO.output(23, False)
        #second loop with new mixup
        if (counter == 20):
            while (counter != 30):
                GPIO.output(11, True)   
                time.sleep(.15)
                GPIO.output(11, False)
                time.sleep(.15)
                GPIO.output(13, True)
                time.sleep(.15)
                GPIO.output(13, False)
                time.sleep(.15)
                GPIO.output(15, True)
                time.sleep(.15)
                GPIO.output(15, False)
                
                if (counter >= 20 & counter <= 30):
                    GPIO.output(19, True)   
                    time.sleep(.08)
                    GPIO.output(19, False)
                    time.sleep(.1)
                    GPIO.output(21, True)
                    time.sleep(.08)
                    GPIO.output(21, False)
                    time.sleep(.08)
                    GPIO.output(23, True)
                    time.sleep(.08)
                    GPIO.output(23, False)
                counter += 1
        #3rd loop
        if (counter == 40):
            while (counter != 50):
                GPIO.output(11, True)
                GPIO.output(23, True)
                time.sleep(.1)
                GPIO.output(11, False)
                GPIO.output(23, False)
                time.sleep(.1)
                GPIO.output(13, True)
                GPIO.output(21, True)
                time.sleep(.1)
                GPIO.output(13, False)
                GPIO.output(21, False)
                time.sleep(.1)
                GPIO.output(15, True)
                GPIO.output(19, True)
                time.sleep(.1)
                GPIO.output(15, False)
                GPIO.output(19, False)
                counter += 1
        if (counter == 60):    
            while (counter != 70):
                GPIO.output(15, True)
                GPIO.output(19, True)
                time.sleep(.1)
                GPIO.output(15, False)
                GPIO.output(19, False)
                time.sleep(.1)
                GPIO.output(13, True)
                GPIO.output(21, True)
                time.sleep(.1)
                GPIO.output(13, False)
                GPIO.output(21, False)
                time.sleep(.1)
                GPIO.output(11, True)
                GPIO.output(23, True)
                time.sleep(.1)
                GPIO.output(11, False)
                GPIO.output(23, False)
                counter += 1
        counter += 1
except KeyboardInterrupt:
    pass

print counter

GPIO.cleanup()
