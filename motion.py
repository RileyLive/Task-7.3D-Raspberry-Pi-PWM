import time
import RPi.GPIO as GPIO

TRIG = 40
ECHO = 38
BUZZ = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(BUZZ, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setwarnings(False)

pwmbuzz = GPIO.PWM(BUZZ, 2000)
pwmbuzz.start(1)


def distances():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    starttime = time.time()
    stoptime = time.time()

    while GPIO.input(ECHO) == 0:
        starttime = time.time()

    while GPIO.input(ECHO) == 1:
        stoptime = time.time()

    timeDistance = stoptime - starttime
    distances = timeDistance * 17000

    return distances


try:
    while True:
        length = distances()
        if length < 100:
            pwmbuzz.ChangeDutyCycle(length)
            print("the distance", length)
        time.sleep(0.1)
except KeyboardInterrupt:
    pwmbuzz.ChangeDutyCycle(0)
    print("end")
    GPIO.cleanup() 