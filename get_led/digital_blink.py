import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LED = 26

GPIO.setup(LED, GPIO.OUT)

STATE = 0
period = 1.0

while True:
    GPIO.output(LED, STATE)
    STATE = not STATE
    time.sleep(period)