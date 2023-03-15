import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    print('Enter period of triangle signal')
    period = int(input())
    time_sleep = period/(256*2)
    while True:
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(time_sleep)
        for i in range(255, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(time_sleep)
        #print('Do you want to exit? y/n')
        #if (input() == 'y'):
         #   break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()