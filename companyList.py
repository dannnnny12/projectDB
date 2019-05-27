# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'companyList.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.companyName = QtWidgets.QListView(Dialog)
        self.companyName.setGeometry(QtCore.QRect(20, 100, 111, 192))
        self.companyName.setObjectName("companyName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 190, 58, 15))
        self.label_2.setObjectName("label_2")
        self.companyDetailList = QtWidgets.QListView(Dialog)
        self.companyDetailList.setGeometry(QtCore.QRect(185, 100, 201, 192))
        self.companyDetailList.setObjectName("companyDetailList")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Our Companies"))
        self.label_2.setText(_translate("Dialog", ">>>"))


