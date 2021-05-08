import paho.mqtt.client as mqtt
import json
import os
import sys
import random
import webdav3.client as wc
from datetime import datetime
import time
# The callback for when the client receives a CONNACK response from the server.
class Cloud():
    def __init__(self):
        self.http = 'https://webdav.yandex.ru',
        self.login = 'cloud.samsung',
        self.password = 'samsungclo'

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    def file_write(self, file_hum, file_temp,file_pres, hum, temp, pres):
        if not os.path.exists(file_hum):
            with open(file_hum, 'w'):
                print('File create: ', file_hum)
        if not os.path.exists(file_temp):
            with open(file_temp, 'w'):
                print('File create: ', file_temp)
        if not os.path.exists(file_pres):
            with open(file_pres, 'w'):
                print('File create: ', file_pres)

        for file in [[file_hum, hum],[file_temp, temp], [file_pres, pres]]:
            with open(file[0], 'a') as f:
                time_now = str(datetime.now()).replace(':', '.')[10:-7]
                f.write(str(file[1]) + str(' ') + str(time_now) + '\n')

    # The callback for when a PUBLISH message is received from the server.
    def send_file_to_cloud(self, file_hum, file_temp, file_pres):
        size_hum = os.path.getsize(file_hum)
        size_temp = os.path.getsize(file_temp)
        size_pres = os.path.getsize(file_pres)


        if ((size_hum < 2000) and (size_temp < 2000) and (size_temp < 2000)):
            print('size: ', size_hum, size_temp, size_pres)
        else:
            #print('Prepare to send')
            time_now = str(datetime.now()).replace(':', '.')[10:-7]
            hum_cloud = '/hum' + time_now + '.txt'
            temp_cloud = '/temp' + time_now + '.txt'
            pres_cloud = '/pres' + time_now + '.txt'
            
            options = {
                'webdav_hostname': 'https://webdav.yandex.ru',
                'webdav_login': 'samsung.cloud',
                'webdav_password': 'samsungclo',
            }
            #print('yandex connect')
            client_yandex = wc.Client(options)
            #print(client_yandex.info("cloud1/"))
            #print(client_yandex.check("cloud/"))
            
            for clo in [[hum_cloud, file_hum], [temp_cloud, file_temp], [pres_cloud, file_pres]]:
                remote_path = 'cloud1/'+ str(datetime.now())[:11]
                if not client_yandex.check(remote_path):
                    client_yandex.mkdir(remote_path)
                client_yandex.upload_sync(remote_path=remote_path + clo[0], local_path=clo[1])
                time.sleep(10)
                #print(f'send {clo}')
            
            for file_del in [file_hum, file_temp, file_pres]:
                #print('file_delete')
                os.remove(file_del)

    def on_message(self, client, userdata, msg):
        #print(msg.topic+" "+str(msg.payload))
        hum = random.randint(0, 100)
        temp = random.randint(0, 100)
        pres = random.randint(0, 100)
        decoded = json.loads(str(msg.payload.decode('utf-8', 'ignore')))
        print('rand:', hum, temp, pres)
        file_hum = 'hum.txt'
        file_temp ='temp.txt'
        file_pres ='pres.txt'
        self.file_write(file_hum, file_temp, file_pres, hum, temp, pres)
        self.send_file_to_cloud(file_hum, file_temp, file_pres)
    def mqtt(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect("iot.eclipse.org", 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()

if __name__ == "__main__":
    cl = Cloud()
    cl.mqtt()
