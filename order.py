# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_order(object):
    def setupUi(self, order):
        order.setObjectName("order")
        order.resize(446, 334)
        self.itName = QtWidgets.QTextEdit(order)
        self.itName.setGeometry(QtCore.QRect(160, 70, 141, 21))
        self.itName.setObjectName("itName")
        self.label = QtWidgets.QLabel(order)
        self.label.setGeometry(QtCore.QRect(50, 70, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(order)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.itAmount = QtWidgets.QTextEdit(order)
        self.itAmount.setGeometry(QtCore.QRect(160, 140, 141, 21))
        self.itAmount.setObjectName("itAmount")
        self.label_3 = QtWidgets.QLabel(order)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(order)
        self.label_4.setGeometry(QtCore.QRect(50, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.itNumber = QtWidgets.QTextEdit(order)
        self.itNumber.setGeometry(QtCore.QRect(160, 110, 141, 21))
        self.itNumber.setObjectName("itNumber")
        self.itPayMethod = QtWidgets.QTextEdit(order)
        self.itPayMethod.setGeometry(QtCore.QRect(160, 180, 141, 21))
        self.itPayMethod.setObjectName("itPayMethod")
        self.itOrder = QtWidgets.QPushButton(order)
        self.itOrder.setGeometry(QtCore.QRect(220, 260, 75, 23))
        self.itOrder.setObjectName("itOrder")
        self.itCancel = QtWidgets.QPushButton(order)
        self.itCancel.setGeometry(QtCore.QRect(80, 260, 91, 23))
        self.itCancel.setObjectName("itCancel")

        self.retranslateUi(order)
        QtCore.QMetaObject.connectSlotsByName(order)

    def retranslateUi(self, order):
        _translate = QtCore.QCoreApplication.translate
        order.setWindowTitle(_translate("order", "Form"))
        self.label.setText(_translate("order", "Items name:"))
        self.label_2.setText(_translate("order", "Amount:"))
        self.label_3.setText(_translate("order", "Pay Method:"))
        self.label_4.setText(_translate("order", "Items Number:"))
        self.itOrder.setText(_translate("order", "Order"))
        self.itCancel.setText(_translate("order", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    order = QtWidgets.QMainWindow()
    ui = Ui_order()
    ui.setupUi(order)
    order.show()
    sys.exit(app.exec_())

