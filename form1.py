# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.itName = QtWidgets.QTextEdit(Form)
        self.itName.setGeometry(QtCore.QRect(160, 70, 141, 21))
        self.itName.setObjectName("itName")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 70, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.itAmount = QtWidgets.QTextEdit(Form)
        self.itAmount.setGeometry(QtCore.QRect(160, 140, 141, 21))
        self.itAmount.setObjectName("itAmount")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.itNumber = QtWidgets.QTextEdit(Form)
        self.itNumber.setGeometry(QtCore.QRect(160, 110, 141, 21))
        self.itNumber.setObjectName("itNumber")
        self.itPayMethod = QtWidgets.QTextEdit(Form)
        self.itPayMethod.setGeometry(QtCore.QRect(160, 180, 141, 21))
        self.itPayMethod.setObjectName("itPayMethod")
        self.itOrder = QtWidgets.QPushButton(Form)
        self.itOrder.setGeometry(QtCore.QRect(220, 260, 75, 23))
        self.itOrder.setObjectName("itOrder")
        self.itCancel = QtWidgets.QPushButton(Form)
        self.itCancel.setGeometry(QtCore.QRect(80, 260, 75, 23))
        self.itCancel.setObjectName("itCancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Items name:"))
        self.label_2.setText(_translate("Form", "Amount:"))
        self.label_3.setText(_translate("Form", "Pay Method:"))
        self.label_4.setText(_translate("Form", "Items Number:"))
        self.itOrder.setText(_translate("Form", "Order"))
        self.itCancel.setText(_translate("Form", "Cance"))


