import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LIGHT = 23

GPIO.setup(LIGHT, GPIO.OUT)

SWITCH = 13
GPIO.setup(SWITCH, GPIO.IN)

STATE = 0

while True:
    if GPIO.input(SWITCH):
        STATE = not STATE
        GPIO.output(LIGHT, STATE)
        time.sleep(0.2)

        