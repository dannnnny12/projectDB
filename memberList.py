# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memberList.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.memName = QtWidgets.QListView(Dialog)
        self.memName.setGeometry(QtCore.QRect(20, 70, 121, 221))
        self.memName.setObjectName("memName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 170, 41, 16))
        self.label_2.setObjectName("label_2")
        self.memDetailList = QtWidgets.QListView(Dialog)
        self.memDetailList.setGeometry(QtCore.QRect(200, 70, 191, 221))
        self.memDetailList.setObjectName("memDetailList")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Members List"))
        self.label_2.setText(_translate("Dialog", ">>>"))


