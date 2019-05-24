# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 460)
        self.welcome = QtWidgets.QLabel(Dialog)
        self.welcome.setGeometry(QtCore.QRect(100, 20, 331, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.viewOurItems = QtWidgets.QPushButton(Dialog)
        self.viewOurItems.setGeometry(QtCore.QRect(170, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.viewOurItems.setFont(font)
        self.viewOurItems.setObjectName("viewOurItems")
        self.viewOurCompanies = QtWidgets.QPushButton(Dialog)
        self.viewOurCompanies.setGeometry(QtCore.QRect(150, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.viewOurCompanies.setFont(font)
        self.viewOurCompanies.setObjectName("viewOurCompanies")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.placeAnOrder = QtWidgets.QPushButton(Dialog)
        self.placeAnOrder.setGeometry(QtCore.QRect(160, 330, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.placeAnOrder.setFont(font)
        self.placeAnOrder.setObjectName("placeAnOrder")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome.setText(_translate("Dialog", "Welcome to Our Market"))
        self.viewOurItems.setText(_translate("Dialog", "View our Items"))
        self.viewOurCompanies.setText(_translate("Dialog", "View Our Companies"))
        self.pushButton.setText(_translate("Dialog", "Purchasing History"))
        self.placeAnOrder.setText(_translate("Dialog", "Place an Order"))


