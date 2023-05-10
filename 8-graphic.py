from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

with open('settings.txt') as file:
    settings=[float(i) for i in file.read().split('\n')]

data=numpy.loadtxt('data.txt', dtype=int) * 3.3/256

data_time=numpy.array([i*settings[0] for i in range(data.size)])

fig, ax=pyplot.subplots(figsize=(16, 10), dpi=1000)

ax.axis([data_time.min(), data_time.max(), data.min(), data.max()])

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC цепи', 60)), fontsize=30, loc = 'center')

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.set_ylabel("Напряжение, В", fontsize=20)
ax.set_xlabel("Время, с", fontsize=20)

ax.plot(data_time, data, c='black', linewidth=2, label = 'V(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'blue', s=2)

ax.legend(shadow = False, loc = 'right', fontsize = 30)

fig.savefig('graph.png')
fig.savefig('graph.svg')