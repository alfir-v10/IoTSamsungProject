
import matplotlib.pyplot as plt  #
import matplotlib.animation as animation
import webdav3.client as wc
import time
import re
eui = ['807B85902000059E', '807B8590200005AF', '807B8590200005D9']
def poit(eui1, eui2, val,l=0):
    def check_file_on_cloud(hum):
        print('check')
        options = {
            'webdav_hostname': "https://webdav.yandex.ru",
            'webdav_login': "samsung.cloud",
            'webdav_password': "samsungclo"
        }
        client = wc.Client(options)
        if client.check(hum):
            client.download_sync(remote_path=f'{hum}', local_path=f'{hum}')
            with open(hum, 'r') as f:
                h1 = [re.split(' ', k) for k in f.readlines()][0]
            return h1
        else:
            print('sleep')
            time.sleep(20)
            check_file_on_cloud(hum)


    def data_gen(t=0):
        print('data')
        cnt = 0
        while cnt < 10000:
            hum = f'cloud1/real/{eui}/{val}_real.txt'
            h1 = check_file_on_cloud(hum)
            t += 1
            cnt += 1
            options = {
                'webdav_hostname': "https://webdav.yandex.ru",
                'webdav_login': "samsung.cloud",
                'webdav_password': "samsungclo"
            }
            client = wc.Client(options)
            client.clean(hum)
            print('clean')
            yield t, float(h1[0])

    def init():
        print('init')
        ax.set_ylim(15, 40)
        ax.set_xlim(0, 100)
        del xdata[:]
        del ydata[:]
        line.set_data(xdata, ydata)
        ax.relim()
        return line,

    def run(data):
        print('run')
        # update the data
        t, y = data
        print(t,y)
        xdata.append(t)
        ydata.append(y)
        xmin, xmax = ax.get_xlim()
        #print(type(t), type(xmax))
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
        line.set_data(xdata, ydata)
        return line

    return run, data_gen, init


hum = 'hum'
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
ani1 = animation.FuncAnimation(fig, poit(eui[2],hum)[0], poit(eui[2], hum)[1], blit=False, interval=30000,
                              repeat=False, init_func=poit(eui[2], hum)[2])

plt.show()