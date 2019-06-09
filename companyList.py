# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'companyList.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_company(object):
    def setupUi(self, company):
        company.setObjectName("company")
        company.resize(400, 300)
        self.companyName = QtWidgets.QListView(company)
        self.companyName.setGeometry(QtCore.QRect(20, 100, 111, 192))
        self.companyName.setObjectName("companyName")
        self.label = QtWidgets.QLabel(company)
        self.label.setGeometry(QtCore.QRect(130, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(company)
        self.label_2.setGeometry(QtCore.QRect(150, 190, 58, 15))
        self.label_2.setObjectName("label_2")
        self.companyDetailList = QtWidgets.QListView(company)
        self.companyDetailList.setGeometry(QtCore.QRect(185, 100, 201, 192))
        self.companyDetailList.setObjectName("companyDetailList")

        self.retranslateUi(company)
        QtCore.QMetaObject.connectSlotsByName(company)

    def retranslateUi(self, company):
        _translate = QtCore.QCoreApplication.translate
        company.setWindowTitle(_translate("company", "Dialog"))
        self.label.setText(_translate("company", "Our Companies"))
        self.label_2.setText(_translate("company", ">>>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    company = QtWidgets.QDialog()
    ui = Ui_company()
    ui.setupUi(company)
    company.show()
    sys.exit(app.exec_())

