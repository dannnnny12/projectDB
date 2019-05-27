# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'items.ui'
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
        self.label.setGeometry(QtCore.QRect(170, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.itemName = QtWidgets.QListView(Dialog)
        self.itemName.setGeometry(QtCore.QRect(20, 80, 131, 201))
        self.itemName.setObjectName("itemName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 170, 58, 15))
        self.label_2.setObjectName("label_2")
        self.itemDetialList = QtWidgets.QListView(Dialog)
        self.itemDetialList.setGeometry(QtCore.QRect(195, 81, 191, 201))
        self.itemDetialList.setObjectName("itemDetialList")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Items"))
        self.label_2.setText(_translate("Dialog", ">>>"))


