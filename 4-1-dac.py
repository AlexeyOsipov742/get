import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        print('Enter a number in range [0,255]')
        value = input()
        if value == 'q':
            break
        else:
            if '.' in value:
                i=0
                s=''
                while (value[i] != '.'):
                    s += value[i]
                    i+=1
                value = int(s)
            else:
                value = int(value)
            print('Entered value = ', value)
            print('Bin value = ', decimal2binary(value))
            print('Current voltage = ', 3.3/256*value)
            GPIO.output(dac, decimal2binary(value))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()