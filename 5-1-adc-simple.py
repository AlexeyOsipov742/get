import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
maxVoltage = 3.3

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc(value):
    return value/256 * maxVoltage

try:
    while True:
        for value in range(256):
            signal = decimal2binary(value)
            GPIO.output(dac, signal)
            voltage = adc(value)
            time.sleep(0.01)
            comp_value = GPIO.input(comp)
            if comp_value == 0:
                print(value, voltage)
                break
finally:
    GPIO.output([26, 19, 13, 6, 5, 11, 9, 10], 0)
    GPIO.cleanup()