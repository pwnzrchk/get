import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = 23
GPIO.setup(LED, GPIO.OUT)
DIV = 6

GPIO.setup(DIV, GPIO.IN)
while True:
    GPIO.output(LED, (not (GPIO.input(DIV))))