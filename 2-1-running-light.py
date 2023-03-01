import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]
for i in leds:
    GPIO.setup(i, GPIO.OUT)
#for i in range(len(leds)):
#   print(leds[i])
for j in range(3):
    for i in range(len(leds)-1, -1, -1):
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)
for i in leds:
    GPIO.output(i, 0)
GPIO.cleanup()