# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_voltimetro.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setObjectName("lcd")
        self.verticalLayout.addWidget(self.lcd)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selecionarEntrada = QtWidgets.QComboBox(self.centralwidget)
        self.selecionarEntrada.setObjectName("selecionarEntrada")
        self.horizontalLayout.addWidget(self.selecionarEntrada)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voltimetro"))
        self.label.setText(_translate("MainWindow", "Entrada Analógica:"))

