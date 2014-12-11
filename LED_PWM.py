import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

p1 = GPIO.PWM(11, 25)
p2 = GPIO.PWM(13, 25)
p3 = GPIO.PWM(15, 25)
p4 = GPIO.PWM(19, 75)
p5 = GPIO.PWM(21, 75)
p6 = GPIO.PWM(23, 75)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
p5.start(0)
p6.start(0)

try:
    while True:
        for i in range(50):
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
        for i in range(50):
            p1.ChangeDutyCycle(1)
            p1.ChangeFrequency(5)
            time.sleep(0.02)
            p2.ChangeDutyCycle(1)
            p2.ChangeFrequency(5)
            time.sleep(0.02)
            p3.ChangeDutyCycle(1)
            p3.ChangeFrequency(5)
            time.sleep(0.02)
            p4.ChangeDutyCycle(1)
            p4.ChangeFrequency(5)
            time.sleep(0.02)
            p5.ChangeDutyCycle(1)
            p5.ChangeFrequency(5)
            time.sleep(0.02)
            p6.ChangeDutyCycle(1)
            p6.ChangeFrequency(5)
            time.sleep(0.02)

except KeyboardInterrupt:
    pass

p1.stop()
p2.stop()
p3.stop()
p4.stop()
p5.stop()
p6.stop()

GPIO.cleanup()
