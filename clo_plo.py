import webdav3.client as wc
import time
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import os
import matplotlib.dates as mdates
eui = ['807B8590200005D9', '807B8590200005AF']
def check_file_on_cloud(hum1, hum2, temp1, temp2, tm1, tm2, tm3, tm4):
    print('Проверяем файлы на облаке')
    options = {
        'webdav_hostname': "https://webdav.yandex.ru",
        'webdav_login': "samsung.cloud",
        'webdav_password': "samsungclo"
    }
    client = wc.Client(options)
    Tr = True
    while Tr:
        if (client.check(hum1) and client.check(hum2) and client.check(temp1) and client.check(temp2)):
            print('Файлы на облаке присутствуют')
            for k in [f'cloud1/real/{eui[0]}/',f'cloud1/real/{eui[1]}/']:
                if not os.path.exists(k):
                    os.makedirs(k)
            for k in [hum1, hum2, temp1, temp2]:
                client.download_sync(remote_path=f'{k}', local_path=f'{k}')
            print('Cкачиваем файлы с облака')
            with open(hum1, 'r') as f:
                s = [re.split(' ', k) for k in f.readlines()]
                h1= float(s[0][0])
                time1 = s[0][1]
            with open(hum2, 'r') as f:
                s = [re.split(' ', k) for k in f.readlines()]
                h2=float(s[0][0])
                time2 = s[0][1]
            with open(temp1, 'r') as f:
                s = [re.split(' ', k) for k in f.readlines()]
                t1 = float(s[0][0])
                time3 = s[0][1]
            with open(temp2, 'r') as f:
                s = [re.split(' ', k) for k in f.readlines()]
                t2 = float(s[0][0])
                time4 = s[0][1]
            print('Файлы скачались с облака')
            print('Сравниваем время ')
            print(tm1, time1)
            print(tm2, time2)
            print(tm3, time3)
            print(tm4, time4)
            if ((tm1 != time1) and (tm2 != time2) and (tm3 != time3) and (tm4 != time4)):
                print('Данные считались')
                Tr = False
                return h1, h2, t1, t2, time1, time2, time3, time4
        else:
            print('Ждем новые данные')
            time.sleep(5)


def data_gen(t=0):
    tm1 = tm2 = tm3 = tm4 = '0'
    cnt = 0
    eui = ['807B8590200005D9', '807B8590200005AF']
    while cnt < 1000000:
        hum1 = f'cloud1/real/{eui[0]}/hum_real.txt'
        hum2 = f'cloud1/real/{eui[1]}/hum_real.txt'
        temp1 = f'cloud1/real/{eui[0]}/temp_real.txt'
        temp2 = f'cloud1/real/{eui[1]}/temp_real.txt'
        h1, h2, t1, t2, tm1, tm2, tm3, tm4 = check_file_on_cloud(hum1, hum2, temp1, temp2, tm1, tm2, tm3, tm4)
        cnt += 1
        t += 0.1
        date = np.datetime64(datetime.now())
        date1 = np.datetime64((str(date)[0:11]+tm1))
        date2 = np.datetime64((str(date)[0:11] + tm2))
        yield date1, date2, h1, h2, t1, t2


def init():
    ax1.set_ylim(0, 50)
    ax2.set_ylim(0, 50)
    datemin = np.datetime64(datetime.now())
    datemax = np.datetime64(datetime.now()) + np.timedelta64(1, 'h')
    ax1.set_xlim(datemin, datemax)
    ax2.set_xlim(datemin, datemax)

    ax1.tick_params(axis='x', which='both', labelsize=8, labelrotation=45)
    ax2.tick_params(axis='x', which='both', labelsize=8, labelrotation=45)
    for k in [xdata1, xdata2, ydata1,ydata2,ydata3,ydata4]:
        del k[:]

    for k in [[line1,xdata1,ydata1],[line2,xdata2,ydata2],[line3,xdata1,ydata3],[line4,xdata2,ydata4]]:
        k[0].set_data(k[1], k[2])
    return line1, line2, line3, line4


def run(data):
    t1,t2, y1, y2, y3, y4 = data
    xdata1.append(t1)
    xdata2.append(t2)
    ydata1.append(y1)
    ydata2.append(y2)
    ydata3.append(y3)
    ydata4.append(y4)
    line1.set_data(xdata1, ydata1)
    line2.set_data(xdata2,ydata2)
    line3.set_data(xdata1, ydata3)
    line4.set_data(xdata2, ydata4)
    return line1, line2, line3, line4

fig, (ax1, ax2) = plt.subplots(figsize =(20,10), nrows=2, ncols=1)
line1, = ax1.plot([], [], '*', lw=1)
line2, = ax1.plot([], [], 'H', lw=1)
line3, = ax2.plot([], [], '*', lw=1)
line4, = ax2.plot([], [], 'H', lw=1)
ax1.grid()
ax2.grid()
ax1.set_title('Температура и Влажность')
ax2.set_ylabel('Температура, \u2103')
ax1.set_ylabel('Влажность, %')
ax2.set_xlabel('Время')
ax1.set_xlabel('Время')
xdata1, xdata2, ydata1, ydata2, ydata3, ydata4 = [], [], [], [], [], []
fig.legend((line1, line2), (f'{eui[0]}', f'{eui[1]}'), 'upper right')
fig.legend((line3,line4), (f'{eui[0]}', f'{eui[1]}'), 'lower right')
years = mdates.YearLocator()
months = mdates.MonthLocator()
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
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=60*1000,
                              repeat=False, init_func=init)
plt.show()

