from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QObject, pyqtSignal
from GUIPLOT import Ui_MainWindow
import sys
from bs4 import BeautifulSoup as bs
import requests
import webdav3.client as wc
import re
from datetime import datetime
import os

class MainWindow(QtWidgets.QMainWindow, QObject, Ui_MainWindow,QImage):
    def __init__(self):
        super().__init__()
        self.url = 'https://yandex.ru/pogoda/kazan'
        self.eui = ['807B8590200005D9', '807B8590200005AF']
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
        page = requests.get(self.url)
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
        self.y_temp.setText(str(today_temp))
        self.y_speed.setText(str(today_wind_speed)+' м/с')
        self.y_vect.setText(str(today_wind_vect))
        self.y_hum.setText(str(today_humid))
        self.y_pres.setText(str(today_pressur))
        self.y_condit.setText(str(today_condit))
        self.y_time.setText(str(time_now))
        self.y_date.setText(str(today_now))
    def changeTitle(self):
        self.yandex_whether()
        cloud_path = 'cloud1/real/'
        eui_init = {}
        for k in self.eui:
            hum = cloud_path+f'{k}/hum_real.txt'
            temp = cloud_path + f'{k}/temp_real.txt'
            pres = cloud_path + f'{k}/pres_real.txt'
            lum = cloud_path + f'{k}/lum_real.txt'
            eui_init.update({k: [hum, temp, pres, lum]})
        print(eui_init)
        if self.ui.checkBox.checkState():
            options = {
                'webdav_hostname': "https://webdav.yandex.ru",
                'webdav_login': "samsung.cloud",
                'webdav_password': "samsungclo"
            }
            client = wc.Client(options)

            for eui, bme in eui_init.items():
                for val in bme:
                    print(val)
                    if client.check(val):
                        client.download_sync(remote_path=f'{val}', local_path=f'{val}')
                        print('pass')
                        #QtCore.QTimer.singleShot(10 * 1000, self.changeTitle)
                    else:
                        print('shot')
                        QtCore.QTimer.singleShot(10*1000, self.changeTitle)
            print('continue')

            for k in [f'cloud1/real/{self.eui[0]}/', f'cloud1/real/{self.eui[1]}/']:
                if not os.path.exists(k):
                    os.makedirs(k)

app = QtWidgets.QApplication(sys.argv)
mainapp = MainWindow()
mainapp.show()
sys.exit(app.exec())