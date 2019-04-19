# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCamera.setGeometry(QtCore.QRect(0, 420, 89, 25))
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapture.setGeometry(QtCore.QRect(110, 420, 89, 25))
        self.btnCapture.setObjectName("btnCapture")
        self.btnReadImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnReadImage.setGeometry(QtCore.QRect(250, 420, 89, 25))
        self.btnReadImage.setObjectName("btnReadImage")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(80, 100, 150, 150))
        self.labelCamera.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setGeometry(QtCore.QRect(310, 100, 150, 150))
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(580, 100, 150, 150))
        self.labelResult.setObjectName("labelResult")
        self.btnGray = QtWidgets.QPushButton(self.centralwidget)
        self.btnGray.setGeometry(QtCore.QRect(360, 420, 89, 25))
        self.btnGray.setObjectName("btnGray")
        self.btnThreshold = QtWidgets.QPushButton(self.centralwidget)
        self.btnThreshold.setGeometry(QtCore.QRect(570, 420, 131, 25))
        self.btnThreshold.setObjectName("btnThreshold")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.btnCapture.clicked.connect(MainWindow.btnCapture_Clicked)
        self.btnReadImage.clicked.connect(MainWindow.btnReadImage_Clicked)
        self.btnGray.clicked.connect(MainWindow.btnGray_Clicked)
        self.btnThreshold.clicked.connect(MainWindow.btnThreshold_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpenCamera.setText(_translate("MainWindow", "打开摄像头"))
        self.btnCapture.setText(_translate("MainWindow", "捕获图片"))
        self.btnReadImage.setText(_translate("MainWindow", "打开图片"))
        self.labelCamera.setText(_translate("MainWindow", "摄像头"))
        self.labelCapture.setText(_translate("MainWindow", "捕获图"))
        self.labelResult.setText(_translate("MainWindow", "结果图"))
        self.btnGray.setText(_translate("MainWindow", "灰度化"))
        self.btnThreshold.setText(_translate("MainWindow", "阈值分割(Otsu)"))

