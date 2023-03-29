import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
#GPIO.setup([26, 19, 13, 6, 5, 11, 9], GPIO.OUT, initial=1)

p = GPIO.PWM(22, 1000)
try:
    while True:
        print('Enter the duty cycle')
        duty_cycle = int(input())
        p.start(duty_cycle)
        print(duty_cycle/100*3.3)
        input('Press Enter to stop:')
        p.stop()

finally:
    GPIO.output([26, 19, 13, 6, 5, 11, 9, 10], 0)
    GPIO.cleanup()