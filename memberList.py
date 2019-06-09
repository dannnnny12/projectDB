# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memberList.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_memberList(object):
    def setupUi(self, memberList):
        memberList.setObjectName("memberList")
        memberList.resize(400, 299)
        self.label = QtWidgets.QLabel(memberList)
        self.label.setGeometry(QtCore.QRect(120, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.memName = QtWidgets.QListView(memberList)
        self.memName.setGeometry(QtCore.QRect(20, 70, 121, 221))
        self.memName.setObjectName("memName")
        self.label_2 = QtWidgets.QLabel(memberList)
        self.label_2.setGeometry(QtCore.QRect(170, 170, 41, 16))
        self.label_2.setObjectName("label_2")
        self.memDetailList = QtWidgets.QListView(memberList)
        self.memDetailList.setGeometry(QtCore.QRect(200, 70, 191, 221))
        self.memDetailList.setObjectName("memDetailList")

        self.retranslateUi(memberList)
        QtCore.QMetaObject.connectSlotsByName(memberList)

    def retranslateUi(self, memberList):
        _translate = QtCore.QCoreApplication.translate
        memberList.setWindowTitle(_translate("memberList", "Dialog"))
        self.label.setText(_translate("memberList", "Members List"))
        self.label_2.setText(_translate("memberList", ">>>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    memberList = QtWidgets.QMainWindow()
    ui = Ui_memberList()
    ui.setupUi(memberList)
    memberList.show()
    sys.exit(app.exec_())

