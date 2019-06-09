# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soldHistory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_soldHistory(object):
    def setupUi(self, soldHistory):
        soldHistory.setObjectName("soldHistory")
        soldHistory.resize(400, 300)
        self.label = QtWidgets.QLabel(soldHistory)
        self.label.setGeometry(QtCore.QRect(120, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.soldList = QtWidgets.QListView(soldHistory)
        self.soldList.setGeometry(QtCore.QRect(30, 100, 341, 192))
        self.soldList.setObjectName("soldList")
        self.label_2 = QtWidgets.QLabel(soldHistory)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(soldHistory)
        QtCore.QMetaObject.connectSlotsByName(soldHistory)

    def retranslateUi(self, soldHistory):
        _translate = QtCore.QCoreApplication.translate
        soldHistory.setWindowTitle(_translate("soldHistory", "Dialog"))
        self.label.setText(_translate("soldHistory", "Sold History"))
        self.label_2.setText(_translate("soldHistory", "Time/Item/Item\'s Number/Amount/Buyer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    soldHistory = QtWidgets.QMainWindow()
    ui = Ui_soldHistory()
    ui.setupUi(soldHistory)
    soldHistory.show()
    sys.exit(app.exec_())

