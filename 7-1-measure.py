import RPi.GPIO as GPIO
import time
from matplotlib import pyplot
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17
maxVoltage = 3.3

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def volts(value):
    return value/256 * maxVoltage

def adc():
    cur_signal = 0
    for i in range(7, -1, -1):
        cur_signal += 2**i
        signal = decimal2binary(cur_signal) 
        GPIO.output(dac, signal)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            cur_signal -= 2**i
    return cur_signal



try:
    cur_signal=0
    result_izm=[]
    time_start=time.time()
    count=0
    while adc() != 0:
        time.sleep(0.01)
    print('начало зарядки конденсатора')
    while cur_signal < 256*0.9:
        cur_signal=adc()
        result_izm.append(cur_signal)
        time.sleep(0.001)
        count+=1
        GPIO.output(leds, decimal2binary(cur_signal))
        voltage = volts(cur_signal)
        print(cur_signal, voltage)
        '''led_signal = int(cur_signal/10)
        for i in range(led_signal):
            GPIO.output(leds[i], 1)
        for j in range(i+1, 8):
            GPIO.output(leds[j], 0)
        if led_signal == 0:
            GPIO.output(leds, 0)'''
        
    GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)

    print('начало разрядки конденсатора') 
    while cur_signal > 256*0.23:
        cur_signal=adc()
        result_izm.append(cur_signal)
        time.sleep(0.001)
        count+=1
        GPIO.output(leds, decimal2binary(cur_signal))
        voltage = volts(cur_signal)
        print(cur_signal, voltage)
        '''led_signal = int(cur_signal/10)
        for i in range(led_signal):
            GPIO.output(leds[i], 1)
        for j in range(i+1, 8):
            GPIO.output(leds[j], 0)
        if led_signal == 0:
            GPIO.output(leds, 0)
        GPIO.output(leds, decimal2binary(cur_signal))'''

    time_experiment=time.time()-time_start

    with open('data.txt', 'w') as f:
        for i in result_izm:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.0114')
    
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/time_experiment/count, 0.01))

    y=[i/256*3.3 for i in result_izm]
    x=[i*time_experiment/count for i in range(len(result_izm))]
    pyplot.plot(x, y)
    pyplot.xlabel('время')
    pyplot.ylabel('вольтаж')
    pyplot.show()
finally:
    GPIO.output([26, 19, 13, 6, 5, 11, 9, 10], 0)
    GPIO.cleanup()