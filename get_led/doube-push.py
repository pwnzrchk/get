import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

UP = 9
DOWN = 10

GPIO.setup(UP, GPIO.IN)
GPIO.setup(DOWN, GPIO.IN)

NUM = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:

    btn_up = GPIO.input(UP)
    btn_down = GPIO.input(DOWN)

    if btn_up and btn_down:
        NUM = 256
        print(NUM, dec2bin(NUM))
        time.sleep(sleep_time)
    
    elif btn_up:
        NUM += 1
        if NUM > 256:
            NUM = 0
        print(NUM, dec2bin(NUM))
        time.sleep(sleep_time)

    if GPIO.input(DOWN):
        NUM -= 1
        if NUM < 0:
            NUM = 0
        print(NUM, dec2bin(NUM))
        time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(NUM))