import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

num = int(input()) % 256

bin_num = '{:08b}'.format(num)
print(num,' = ', bin_num)

number = list(map(int, bin_num))
print(number)
#number = [0, 0, 0, 0, 0, 0, 0, 1]
#for i in range(len(dac)):
#    number.append(random.randint(0, 1))
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)

time.sleep(10)

GPIO.output(dac, 0)

GPIO.cleanup()

