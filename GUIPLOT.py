# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 381)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 381))
        MainWindow.setMaximumSize(QtCore.QSize(700, 381))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background-color: white')
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        #self.verticalLayoutWidget.setStyleSheet({'border: 1px solid black'})
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_11.addWidget(self.checkBox)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 1500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: black")
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.temperature_main = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.temperature_main.setFont(font)
        self.temperature_main.setStyleSheet("color: black")
        self.temperature_main.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_main.setObjectName("temperature_main")
        self.verticalLayout_16.addWidget(self.temperature_main)
        self.val_mean_temp = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_mean_temp.setFont(font)
        self.val_mean_temp.setStyleSheet("color: black")
        self.val_mean_temp.setText("")
        self.val_mean_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.val_mean_temp.setObjectName("val_mean_temp")
        self.verticalLayout_16.addWidget(self.val_mean_temp)
        self.horizontalLayout_17.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.humidity_main = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.humidity_main.setFont(font)
        self.humidity_main.setStyleSheet("color: black")
        self.humidity_main.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity_main.setObjectName("humidity_main")
        self.verticalLayout_17.addWidget(self.humidity_main)
        self.val_mean_humid = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_mean_humid.setFont(font)
        self.val_mean_humid.setStyleSheet("color: black")
        self.val_mean_humid.setText("")
        self.val_mean_humid.setAlignment(QtCore.Qt.AlignCenter)
        self.val_mean_humid.setObjectName("val_mean_humid")
        self.verticalLayout_17.addWidget(self.val_mean_humid)
        self.horizontalLayout_17.addLayout(self.verticalLayout_17)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pressure_main = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pressure_main.setFont(font)
        self.pressure_main.setStyleSheet("color: black")
        self.pressure_main.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_main.setObjectName("pressure_main")
        self.verticalLayout_13.addWidget(self.pressure_main)
        self.val_mean_pres = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_mean_pres.setFont(font)
        self.val_mean_pres.setStyleSheet("color: black")
        self.val_mean_pres.setText("")
        self.val_mean_pres.setTextFormat(QtCore.Qt.AutoText)
        self.val_mean_pres.setAlignment(QtCore.Qt.AlignCenter)
        self.val_mean_pres.setObjectName("val_mean_pres")
        self.verticalLayout_13.addWidget(self.val_mean_pres)
        self.horizontalLayout_17.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.weight_main = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.weight_main.setFont(font)
        self.weight_main.setStyleSheet("color: black")
        self.weight_main.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_main.setObjectName("weight_main")
        self.verticalLayout_14.addWidget(self.weight_main)
        self.val_mean_weig = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_mean_weig.setFont(font)
        self.val_mean_weig.setStyleSheet("color: black")
        self.val_mean_weig.setText("")
        self.val_mean_weig.setAlignment(QtCore.Qt.AlignCenter)
        self.val_mean_weig.setObjectName("val_mean_weig")
        self.verticalLayout_14.addWidget(self.val_mean_weig)
        self.horizontalLayout_17.addLayout(self.verticalLayout_14)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.vibration_main = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.vibration_main.setFont(font)
        self.vibration_main.setStyleSheet("color: black")
        self.vibration_main.setAlignment(QtCore.Qt.AlignCenter)
        self.vibration_main.setObjectName("vibration_main")
        self.verticalLayout_10.addWidget(self.vibration_main)
        self.val_mean_vibr = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_mean_vibr.setFont(font)
        self.val_mean_vibr.setStyleSheet("color: black")
        self.val_mean_vibr.setText("")
        self.val_mean_vibr.setAlignment(QtCore.Qt.AlignCenter)
        self.val_mean_vibr.setObjectName("val_mean_vibr")
        self.verticalLayout_10.addWidget(self.val_mean_vibr)
        self.horizontalLayout_17.addLayout(self.verticalLayout_10)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.luminosity_main = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.luminosity_main.setFont(font)
        self.luminosity_main.setStyleSheet("color: black")
        self.luminosity_main.setAlignment(QtCore.Qt.AlignCenter)
        self.luminosity_main.setObjectName("luminosity_main")
        self.verticalLayout_15.addWidget(self.luminosity_main)
        self.val_mean_lum = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_mean_lum.setFont(font)
        self.val_mean_lum.setStyleSheet("color: black")
        self.val_mean_lum.setText("")
        self.val_mean_lum.setAlignment(QtCore.Qt.AlignCenter)
        self.val_mean_lum.setObjectName("val_mean_lum")
        self.verticalLayout_15.addWidget(self.val_mean_lum)
        self.horizontalLayout_17.addLayout(self.verticalLayout_15)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 551, 243))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: black")
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: black")
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: black")
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: black")
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: black")
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: black")
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: black")
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: black")
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.yandex_data = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_data.setFont(font)
        self.yandex_data.setStyleSheet("color: black")
        self.yandex_data.setText("")
        self.yandex_data.setObjectName("yandex_data")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.yandex_data)
        self.yandex_time = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_time.setFont(font)
        self.yandex_time.setStyleSheet("color: black")
        self.yandex_time.setText("")
        self.yandex_time.setObjectName("yandex_time")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yandex_time)
        self.yandex_condit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_condit.setFont(font)
        self.yandex_condit.setStyleSheet("color: black")
        self.yandex_condit.setText("")
        self.yandex_condit.setObjectName("yandex_condit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yandex_condit)
        self.yandex_temp = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_temp.setFont(font)
        self.yandex_temp.setStyleSheet("color: black")
        self.yandex_temp.setText("")
        self.yandex_temp.setObjectName("yandex_temp")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.yandex_temp)
        self.yandex_hum = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_hum.setFont(font)
        self.yandex_hum.setStyleSheet("color: black")
        self.yandex_hum.setText("")
        self.yandex_hum.setObjectName("yandex_hum")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.yandex_hum)
        self.yandex_pres = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_pres.setFont(font)
        self.yandex_pres.setStyleSheet("color: black")
        self.yandex_pres.setText("")
        self.yandex_pres.setObjectName("yandex_pres")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.yandex_pres)
        self.yandex_speed = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_speed.setFont(font)
        self.yandex_speed.setStyleSheet("color: black")
        self.yandex_speed.setText("")
        self.yandex_speed.setObjectName("yandex_speed")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.yandex_speed)
        self.yandex_vect = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.yandex_vect.setFont(font)
        self.yandex_vect.setStyleSheet("color: black")
        self.yandex_vect.setText("")
        self.yandex_vect.setObjectName("yandex_vect")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.yandex_vect)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ulei_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ulei_1.setFont(font)
        self.ulei_1.setStyleSheet("color: black")
        self.ulei_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ulei_1.setObjectName("ulei_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ulei_1)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: black")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.humidity_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.humidity_1.setFont(font)
        self.humidity_1.setStyleSheet("color: black")
        self.humidity_1.setObjectName("humidity_1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.humidity_1)
        self.pressure_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pressure_1.setFont(font)
        self.pressure_1.setStyleSheet("color: black")
        self.pressure_1.setObjectName("pressure_1")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pressure_1)
        self.weight_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.weight_1.setFont(font)
        self.weight_1.setStyleSheet("color: black")
        self.weight_1.setObjectName("weight_1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.weight_1)
        self.vibration_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.vibration_1.setFont(font)
        self.vibration_1.setStyleSheet("color: black")
        self.vibration_1.setObjectName("vibration_1")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.vibration_1)
        self.luminosity_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.luminosity_1.setFont(font)
        self.luminosity_1.setStyleSheet("color: black")
        self.luminosity_1.setObjectName("luminosity_1")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.luminosity_1)
        self.temperature_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.temperature_1.setFont(font)
        self.temperature_1.setStyleSheet("color: black")
        self.temperature_1.setObjectName("temperature_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.temperature_1)
        self.val_now_temp_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_temp_1.setFont(font)
        self.val_now_temp_1.setStyleSheet("color: black")
        self.val_now_temp_1.setText("")
        self.val_now_temp_1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_temp_1.setObjectName("val_now_temp_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.val_now_temp_1)
        self.val_now_hum_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_hum_1.setFont(font)
        self.val_now_hum_1.setStyleSheet("color: black")
        self.val_now_hum_1.setText("")
        self.val_now_hum_1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_hum_1.setObjectName("val_now_hum_1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.val_now_hum_1)
        self.val_now_pres_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_pres_1.setFont(font)
        self.val_now_pres_1.setStyleSheet("color: black")
        self.val_now_pres_1.setText("")
        self.val_now_pres_1.setTextFormat(QtCore.Qt.AutoText)
        self.val_now_pres_1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_pres_1.setObjectName("val_now_pres_1")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.val_now_pres_1)
        self.val_now_vibr_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_vibr_1.setFont(font)
        self.val_now_vibr_1.setStyleSheet("color: black")
        self.val_now_vibr_1.setText("")
        self.val_now_vibr_1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_vibr_1.setObjectName("val_now_vibr_1")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.val_now_vibr_1)
        self.val_now_weig_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_weig_1.setFont(font)
        self.val_now_weig_1.setStyleSheet("color: black")
        self.val_now_weig_1.setText("")
        self.val_now_weig_1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_weig_1.setObjectName("val_now_weig_1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.val_now_weig_1)
        self.val_now_lum_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_lum_1.setFont(font)
        self.val_now_lum_1.setStyleSheet("color: black")
        self.val_now_lum_1.setText("")
        self.val_now_lum_1.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_lum_1.setObjectName("val_now_lum_1")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.val_now_lum_1)
        self.horizontalLayout_19.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.ulei_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ulei_2.setFont(font)
        self.ulei_2.setStyleSheet("color: black")
        self.ulei_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ulei_2.setObjectName("ulei_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ulei_2)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: black")
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_18)
        self.temperature_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.temperature_2.setFont(font)
        self.temperature_2.setStyleSheet("color: black")
        self.temperature_2.setObjectName("temperature_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.temperature_2)
        self.val_now_temp_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_temp_2.setFont(font)
        self.val_now_temp_2.setStyleSheet("color: black")
        self.val_now_temp_2.setText("")
        self.val_now_temp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_temp_2.setObjectName("val_now_temp_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.val_now_temp_2)
        self.humidity_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.humidity_2.setFont(font)
        self.humidity_2.setStyleSheet("color: black")
        self.humidity_2.setObjectName("humidity_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.humidity_2)
        self.val_now_hum_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_hum_2.setFont(font)
        self.val_now_hum_2.setText("")
        self.val_now_hum_2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_hum_2.setObjectName("val_now_hum_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.val_now_hum_2)
        self.pressure_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pressure_2.setFont(font)
        self.pressure_2.setStyleSheet("color: black")
        self.pressure_2.setObjectName("pressure_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pressure_2)
        self.val_now_pres_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_pres_2.setFont(font)
        self.val_now_pres_2.setStyleSheet("color: black")
        self.val_now_pres_2.setText("")
        self.val_now_pres_2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_pres_2.setObjectName("val_now_pres_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.val_now_pres_2)
        self.weight_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.weight_2.setFont(font)
        self.weight_2.setStyleSheet("color: black")
        self.weight_2.setObjectName("weight_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.weight_2)
        self.val_now_weig_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_weig_2.setFont(font)
        self.val_now_weig_2.setStyleSheet("color: black")
        self.val_now_weig_2.setText("")
        self.val_now_weig_2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_weig_2.setObjectName("val_now_weig_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.val_now_weig_2)
        self.vibration_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.vibration_2.setFont(font)
        self.vibration_2.setStyleSheet("color: black")
        self.vibration_2.setObjectName("vibration_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.vibration_2)
        self.val_now_vibr_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_vibr_2.setFont(font)
        self.val_now_vibr_2.setStyleSheet("color: black")
        self.val_now_vibr_2.setText("")
        self.val_now_vibr_2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_vibr_2.setObjectName("val_now_vibr_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.val_now_vibr_2)
        self.luminosity_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.luminosity_2.setFont(font)
        self.luminosity_2.setStyleSheet("color: black")
        self.luminosity_2.setObjectName("luminosity_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.luminosity_2)
        self.val_now_lum_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.val_now_lum_2.setFont(font)
        self.val_now_lum_2.setStyleSheet("color: black")
        self.val_now_lum_2.setText("")
        self.val_now_lum_2.setAlignment(QtCore.Qt.AlignCenter)
        self.val_now_lum_2.setObjectName("val_now_lum_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.val_now_lum_2)
        self.horizontalLayout_19.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_19)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BeesWorld"))
        self.checkBox.setText(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "?????????????? ?????????????? ???? ??????????"))
        self.temperature_main.setText(_translate("MainWindow", "??????????????????????"))
        self.humidity_main.setText(_translate("MainWindow", "??????????????????"))
        self.pressure_main.setText(_translate("MainWindow", "????????????????"))
        self.weight_main.setText(_translate("MainWindow", "??????"))
        self.vibration_main.setText(_translate("MainWindow", "????????????????"))
        self.luminosity_main.setText(_translate("MainWindow", "????????????????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????.????????????"))
        self.label_3.setText(_translate("MainWindow", "????????"))
        self.label_4.setText(_translate("MainWindow", "??????????"))
        self.label_5.setText(_translate("MainWindow", "??????????????????"))
        self.label_6.setText(_translate("MainWindow", "??????????????????????"))
        self.label_7.setText(_translate("MainWindow", "??????????????????"))
        self.label_8.setText(_translate("MainWindow", "????????????????"))
        self.label_9.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.label_11.setText(_translate("MainWindow", "?????????????????????? ??????????"))
        self.ulei_1.setText(_translate("MainWindow", "???????? 1"))
        self.label_10.setText(_translate("MainWindow", "?????????????? ????????????????"))
        self.humidity_1.setText(_translate("MainWindow", "??????????????????"))
        self.pressure_1.setText(_translate("MainWindow", "????????????????"))
        self.weight_1.setText(_translate("MainWindow", "??????"))
        self.vibration_1.setText(_translate("MainWindow", "????????????????"))
        self.luminosity_1.setText(_translate("MainWindow", "????????????????????????"))
        self.temperature_1.setText(_translate("MainWindow", "??????????????????????"))
        self.ulei_2.setText(_translate("MainWindow", "???????? 2"))
        self.label_18.setText(_translate("MainWindow", "?????????????? ????????????????"))
        self.temperature_2.setText(_translate("MainWindow", "??????????????????????"))
        self.humidity_2.setText(_translate("MainWindow", "??????????????????"))
        self.pressure_2.setText(_translate("MainWindow", "????????????????"))
        self.weight_2.setText(_translate("MainWindow", "??????"))
        self.vibration_2.setText(_translate("MainWindow", "????????????????"))
        self.luminosity_2.setText(_translate("MainWindow", "????????????????????????"))


