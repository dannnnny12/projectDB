# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'items.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_items(object):
    def connect_database():

        db_connect = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'abit850923',
        database = '',
        )
        cursor = db_connect.cursor()
        cursor.execute('SELECT * FROM project.company')
        result = cursor.fetchall()
        company_ID = []
        company_name = []

        for rows in result:
            adjust = list(rows)
            company_ID.append(adjust[0])
            company_name.append(adjust[1])

    def setupUi(self, items):
        items.setObjectName("items")
        items.resize(400, 300)
        self.label = QtWidgets.QLabel(items)
        self.label.setGeometry(QtCore.QRect(170, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.itemName = QtWidgets.QListView(items)
        self.itemName.setGeometry(QtCore.QRect(20, 80, 131, 201))
        self.itemName.setObjectName("itemName")
        self.label_2 = QtWidgets.QLabel(items)
        self.label_2.setGeometry(QtCore.QRect(170, 170, 58, 15))
        self.label_2.setObjectName("label_2")
        self.itemDetialList = QtWidgets.QListView(items)
        self.itemDetialList.setGeometry(QtCore.QRect(195, 81, 191, 201))
        self.itemDetialList.setObjectName("itemDetialList")

        self.retranslateUi(items)
        QtCore.QMetaObject.connectSlotsByName(items)

    def retranslateUi(self, items):
        _translate = QtCore.QCoreApplication.translate
        items.setWindowTitle(_translate("items", "Dialog"))
        self.label.setText(_translate("items", "Items"))
        self.label_2.setText(_translate("items", ">>>"))


if __name__ == "__main__":
    import sys
    connect_database()
    app = QtWidgets.QApplication(sys.argv)
    items = QtWidgets.QMainWindow()
    ui = Ui_items()
    ui.setupUi(items)
    items.show()
    sys.exit(app.exec_())

