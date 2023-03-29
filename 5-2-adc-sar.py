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
        cur_signal = 0
        for i in range(7, -1, -1):
            cur_signal += 2**i
            signal = decimal2binary(cur_signal) 
            GPIO.output(dac, signal)
            voltage = adc(cur_signal)
            time.sleep(0.001)
            comp_value = GPIO.input(comp)
            if comp_value == 0:
                cur_signal -= 2**i
        print(cur_signal, voltage)
finally:
    GPIO.output([26, 19, 13, 6, 5, 11, 9, 10], 0)
    GPIO.cleanup()