from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QObject, pyqtSignal,QSize
from GUIPLOT import Ui_MainWindow
from PyQt5 import QtGui
import sys
from bs4 import BeautifulSoup as bs
import requests
import random
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import matplotlib.dates as mdates
import webdav3.client as wc
import time
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import os
import matplotlib.dates as mdates

class MainWindow(QtWidgets.QMainWindow, QObject, Ui_MainWindow,QImage):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #oImage = QImage('bees.jpg')
        #sImage = oImage.scaled(QSize(558, 381))  # resize Image to widgets size
        #palette = QPalette()
        #palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        #self.setPalette(palette)
        self.signal = pyqtSignal()
        self.mean_temp = self.ui.val_mean_temp
        self.mean_hum = self.ui.val_mean_humid
        self.mean_pres = self.ui.val_mean_pres
        self.mean_weig = self.ui.val_mean_weig
        self.mean_vibr = self.ui.val_mean_vibr
        self.mean_lum = self.ui.val_mean_lum
        self.temp_1 = self.ui.val_now_temp_1
        self.temp_2 = self.ui.val_now_temp_2
        self.hum_1 = self.ui.val_now_hum_1
        self.hum_2 = self.ui.val_now_hum_2
        self.pres_1 = self.ui.val_now_pres_1
        self.pres_2 = self.ui.val_now_pres_2
        self.weig_1 = self.ui.val_now_weig_1
        self.weig_2 = self.ui.val_now_weig_2
        self.vibr_1 = self.ui.val_now_vibr_1
        self.vibr_2 = self.ui.val_now_vibr_2
        self.lum_1 = self.ui.val_now_lum_1
        self.lum_2 = self.ui.val_now_lum_2

        self.y_condit = self.ui.yandex_condit
        self.y_date = self.ui.yandex_data
        self.y_time = self.ui.yandex_time
        self.y_hum = self.ui.yandex_hum
        self.y_temp = self.ui.yandex_temp
        self.y_pres = self.ui.yandex_pres
        self.y_speed = self.ui.yandex_speed
        self.y_vect = self.ui.yandex_vect

        self.ui.checkBox.clicked.connect(self.changeTitle)
        self.ui.checkBox.clicked.connect(self.yandex_whether)
    def yandex_whether(self):
        url = 'https://yandex.ru/pogoda/kazan'
        page = requests.get(url)
        print(page.status_code)
        soup = bs(page.text, 'html.parser')
        s = soup.find('div', class_='fact__props fact__props_position_middle')
        today_temp = soup.find('div', class_='temp fact__temp fact__temp_size_s').get_text()
        today_wind_speed = s.find('span', class_="wind-speed").get_text()
        today_wind_vect = s.find('abbr', class_='icon-abbr').get_text()
        today_humid = s.find('dl', class_='term term_orient_v fact__humidity').get_text()
        today_pressur = s.find('dl', class_='term term_orient_v fact__pressure').get_text()
        today_condit = soup.find('div', class_='link__condition day-anchor i-bem').get_text()
        time_now = str(datetime.now())[11:16]
        today_now = str(datetime.today())[:10]
        #font = QtGui.QFont()
        #font.setFamily("Gloucester MT Extra Condensed")
        #font.setPointSize(12)
        self.y_temp.setText(str(today_temp))
        self.y_speed.setText(str(today_wind_speed))
        self.y_vect.setText(str(today_wind_vect))
        self.y_hum.setText(str(today_humid))
        self.y_pres.setText(str(today_pressur))
        self.y_condit.setText(str(today_condit))
        self.y_time.setText(str(time_now))
        self.y_date.setText(str(today_now))
        #for k in [self.y_temp, self.y_speed, self.y_vect, self.y_hum, self.y_hum,
         #         self.y_pres, self.y_condit, self.y_time, self.y_date]:
          #  k.setFont(font)
    def change_background(self):
        s = random.choice(['bees.jpg','bees1.jpg','bees2.jpg','bees3.jpg'])
        print(s)
        oImage = QImage(s)
        sImage = oImage.scaled(QSize(558, 381))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
    def changeTitle(self):
        self.yandex_whether()
        #self.change_background()
        #датчики
        eui = ['807B8590200005D9', '807B8590200005AF']
        hum1 = f'cloud1/real/{eui[0]}/hum_real.txt'
        hum2 = f'cloud1/real/{eui[1]}/hum_real.txt'
        temp1 = f'cloud1/real/{eui[0]}/temp_real.txt'
        temp2 = f'cloud1/real/{eui[1]}/temp_real.txt'
        pres1 = f'cloud1/real/{eui[0]}/pres_real.txt'
        pres2 = f'cloud1/real/{eui[1]}/pres_real.txt'
        lum1 = f'cloud1/real/{eui[0]}/lum_real.txt'
        lum2 = f'cloud1/real/{eui[1]}/lum_real.txt'
        tm1, tm2, tm3, tm4, tm5, tm6, tm7, tm8 = '0', '0', '0', '0', '0', '0', '0', '0'
        if self.ui.checkBox.checkState():
            #x = random.randint(0,10)
            print('check_file_on_cloud')
            options = {
                'webdav_hostname': "https://webdav.yandex.ru",
                'webdav_login': "samsung.cloud",
                'webdav_password': "samsungclo"
            }
            client = wc.Client(options)
            print(client.check(hum1), client.check(hum2),
                  client.check(temp1), client.check(temp2),
                  client.check(pres1), client.check(pres2),
                  client.check(lum1), client.check(lum2))
            if (client.check(hum1) and client.check(hum2) and
                    client.check(temp1) and client.check(temp2) and
                    client.check(pres1) and client.check(pres2) and
                    client.check(hum1) and client.check(hum2)):
                for k in [f'cloud1/real/{eui[0]}/', f'cloud1/real/{eui[1]}/']:
                    if not os.path.exists(k):
                        os.makedirs(k)
                for k in [hum1, hum2, temp1, temp2, pres1, pres2, lum1, lum2]:
                    client.download_sync(remote_path=f'{k}', local_path=f'{k}')
                with open(hum1, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    h1 = float(s[0][0])
                    time1 = s[0][1]
                with open(hum2, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    h2 = float(s[0][0])
                    time2 = s[0][1]
                with open(temp1, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    t1 = float(s[0][0])
                    time3 = s[0][1]
                with open(temp2, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    t2 = float(s[0][0])
                    time4 = s[0][1]
                with open(pres1, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    p1 = float(s[0][0])
                    time5 = s[0][1]
                with open(pres2, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    p2 = float(s[0][0])
                    time6 = s[0][1]
                with open(lum1, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    l1 = float(s[0][0])
                    time7 = s[0][1]
                with open(lum2, 'r') as f:
                    s = [re.split(' ', k) for k in f.readlines()]
                    l2 = float(s[0][0])
                    time8 = s[0][1]
                print(h1, h2, t1, t2, p1, p2, l1, l2)
                print(f'{time1}:{tm1}\n{time2}:{tm2}\n{time3}:{tm3}\n{time4}:{tm4}\n{time5}:{tm5}\n'
                      f'{time6}:{tm6}\n{time7}:{tm7}\n{time8}:{tm8}')
                if 25 < t1 <27: self.temp_1.setStyleSheet("color: black")
                else: self.temp_1.setStyleSheet("color: red")
                if 25 < t2 < 27: self.temp_2.setStyleSheet("color: black")
                else: self.temp_2.setStyleSheet("color: red")

                if 20 < l1< 50: self.lum_1.setStyleSheet("color: black")
                else: self.lum_1.setStyleSheet("color: red")
                if 20 < l2 < 50: self.lum_2.setStyleSheet("color: black")
                else: self.lum_2.setStyleSheet("color: red")

                if 27< h1 < 30: self.hum_1.setStyleSheet("color: black")
                else: self.hum_1.setStyleSheet("color: red")
                if 27 <h2<30: self.hum_2.setStyleSheet("color: black")
                else: self.hum_2.setStyleSheet("color: red")

                if 1000 < p1 < 1010: self.pres_1.setStyleSheet("color: black")
                else: self.pres_1.setStyleSheet("color: red")
                if 1000 < p2 < 1010: self.pres_2.setStyleSheet("color: black")
                else: self.pres_2.setStyleSheet("color: red")

                self.temp_1.setText(str(t1))
                self.temp_2.setText(str(t2))
                self.hum_1.setText(str(h1) + ' %')
                self.hum_2.setText(str(h2) + ' %')
                self.lum_1.setText(str(l1) + ' лк')
                self.lum_2.setText(str(l2) + ' лк')
                self.pres_1.setText(str(p1))
                self.pres_2.setText(str(p2))
                self.vibr_1.setText('-')
                self.vibr_1.setStyleSheet('background-color: black, color: black')
                self.vibr_2.setText('-')
                self.vibr_2.setStyleSheet('background-color: black, color: black')
                self.weig_1.setText('-')
                self.weig_2.setText('-')
                self.weig_1.setStyleSheet('background-color: black, color: black')
                self.weig_2.setStyleSheet('background-color: black, color: black')
                self.mean_hum.setText('-')
                self.mean_hum.setStyleSheet('background-color: black, color: black')
                self.mean_temp.setText('-')
                self.mean_temp.setStyleSheet('background-color: black, color: black')
                self.mean_lum.setText('-')
                self.mean_lum.setStyleSheet('background-color: black, color: black')
                self.mean_pres.setText('-')
                self.mean_pres.setStyleSheet('background-color: black, color: black')
                self.mean_vibr.setText('-')
                self.mean_vibr.setStyleSheet('background-color: black, color: black')
                self.mean_weig.setText('-')
                self.mean_weig.setStyleSheet('background-color: black, color: black')
                QtCore.QTimer.singleShot(1*60*1000, self.changeTitle)

        else: pass
app = QtWidgets.QApplication(sys.argv)
mainapp = MainWindow()
mainapp.show()
sys.exit(app.exec())