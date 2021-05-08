import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import matplotlib.dates as mdates
def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.01
        date  = np.datetime64(datetime.now())
        print(date)
        yield date,  np.sin(2*np.pi*t),  np.cos(2*np.pi*t), np.cos(2*np.pi*t)

def init():
    ax1.set_ylim(-1, 1)
    #ax1.set_xlim(0, 10)
    ax2.set_ylim(-10, 10)
    #ax2.set_xlim(0, 100)
    datemin = np.datetime64(datetime.now())
    datemax = np.datetime64(datetime.now())+np.timedelta64(1, 'h')
    ax1.set_xlim(datemin, datemax)
    ax2.set_xlim(datemin, datemax)

    ax1.tick_params(axis='x', which = 'both', labelsize = 8, labelrotation = 45)
    ax2.tick_params(axis='x', which = 'both', labelsize = 8, labelrotation = 45)

    del xdata[:]
    del ydata[:]
    del ydata2[:]
    line.set_data(xdata, ydata)
    line2.set_data(xdata, ydata2)
    line3.set_data(xdata, ydata3)
    return line, line2, line3

fig, (ax1, ax2) = plt.subplots(figsize =(10,5), nrows=2, ncols=1)

line, = ax1.plot([], [], lw=1)
line3, = ax1.plot([], [], lw=1)
line2, = ax2.plot([], [], lw=1)
ax1.grid()
ax2.grid()
ax1.set_title('Humidity')
ax2.set_title('Temperature')

xdata, ydata, ydata2, ydata3 = [], [], [], []
fig.legend((line, line3), ('Line 1', 'Line 3'), 'upper right')
fig.legend((line2,), ('Line 2',), 'lower right')
years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month

min = mdates.MinuteLocator()
hours = mdates.HourLocator()
hours_fmt = mdates.DateFormatter('%H')
min_fmt = mdates.DateFormatter('%M')
ax1.xaxis.set_major_locator(hours)
ax1.xaxis.set_major_formatter(hours_fmt)
ax1.xaxis.set_minor_locator(min)
ax1.xaxis.set_minor_formatter(min_fmt)

ax2.xaxis.set_major_locator(hours)
ax2.xaxis.set_major_formatter(hours_fmt)
ax2.xaxis.set_minor_locator(min)
ax2.xaxis.set_minor_formatter(min_fmt)
def run(data):

    t, y, y2, y3 = data
    xdata.append(t)
    ydata.append(y)
    ydata2.append(y2)
    ydata3.append(y3)
    line.set_data(xdata, ydata)
    line2.set_data(xdata,ydata2)
    line3.set_data(xdata, ydata3)
    return line, line2,  line3

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=3000,
                              repeat=False, init_func=init)
plt.show()
