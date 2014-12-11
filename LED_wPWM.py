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
    #intro LED segment
    GPIO.output(11, True)   
    time.sleep(.5)
    GPIO.output(13, True)
    time.sleep(.5)
    GPIO.output(15, True)
    time.sleep(.5)
    GPIO.output(19, True)
    time.sleep(.5)
    GPIO.output(21, True)
    time.sleep(.5)
    GPIO.output(23, True)
    time.sleep(.5)
    GPIO.output(23, False)   
    time.sleep(.5)
    GPIO.output(21, False)
    time.sleep(.5)
    GPIO.output(19, False)
    time.sleep(.5)
    GPIO.output(15, False)
    time.sleep(.5)
    GPIO.output(13, False)
    time.sleep(.5)
    GPIO.output(11, False)
    time.sleep(.5)
    #all off and on
    for x in xrange(0,2):
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(19, False)
        GPIO.output(21, False)
        GPIO.output(23, False)
        time.sleep(.5)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.output(19, True)
        GPIO.output(21, True)
        GPIO.output(23, True)
        time.sleep(.5)
    #main loop
    while (counter != 100):
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
        if (counter == 1 or (counter >= 72 and counter <= 74)):
            #setup PWM
            p1 = GPIO.PWM(11, 75)
            p2 = GPIO.PWM(13, 75)
            p3 = GPIO.PWM(15, 75)
            p4 = GPIO.PWM(19, 75)
            p5 = GPIO.PWM(21, 75)
            p6 = GPIO.PWM(23, 75)
            p1.start(0)
            p2.start(0)
            p3.start(0)
            p4.start(0)
            p5.start(0)
            p6.start(0)
            for i in range(25):
                p1.ChangeDutyCycle(1)
                p1.ChangeFrequency(1)
                time.sleep(0.02)
                p2.ChangeDutyCycle(1)
                p2.ChangeFrequency(1)
                time.sleep(0.02)
                p3.ChangeDutyCycle(1)
                p3.ChangeFrequency(1)
                time.sleep(0.02)
                p4.ChangeDutyCycle(1)
                p4.ChangeFrequency(1)
                time.sleep(0.02)
                p5.ChangeDutyCycle(1)
                p5.ChangeFrequency(1)
                time.sleep(0.02)
                p6.ChangeDutyCycle(1)
                p6.ChangeFrequency(1)
                time.sleep(0.02)
            for i in range(25):
                p1.ChangeDutyCycle(1)
                p1.ChangeFrequency(5)
                time.sleep(0.05)
                p2.ChangeDutyCycle(1)
                p2.ChangeFrequency(5)
                time.sleep(0.05)
                p3.ChangeDutyCycle(1)
                p3.ChangeFrequency(5)
                time.sleep(0.05)
                p4.ChangeDutyCycle(1)
                p4.ChangeFrequency(5)
                time.sleep(0.05)
                p5.ChangeDutyCycle(1)
                p5.ChangeFrequency(5)
                time.sleep(0.05)
                p6.ChangeDutyCycle(1)
                p6.ChangeFrequency(5)
                time.sleep(0.05)
            p1.stop()
            p2.stop()
            p3.stop()
            p4.stop()
            p5.stop()
            p6.stop()    
            counter += 1
        counter += 1
except KeyboardInterrupt:
    pass

print counter

p1.stop()
p2.stop()
p3.stop()
p4.stop()
p5.stop()
p6.stop()

GPIO.cleanup()
