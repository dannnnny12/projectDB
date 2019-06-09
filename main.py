# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from items import Ui_items
class Ui_main(object):
	def openWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui= Ui_items()
		self.ui.setupUi(self.window)
		self.window.show()

	def setupUi(self, main):
		main.setObjectName("main")
		main.resize(536, 372)
		self.welcome = QtWidgets.QLabel(main)
		self.welcome.setGeometry(QtCore.QRect(80, 20, 401, 81))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(22)
		self.welcome.setFont(font)
		self.welcome.setObjectName("welcome")
		self.viewOurItems = QtWidgets.QPushButton(main)
		self.viewOurItems.setGeometry(QtCore.QRect(180, 100, 181, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.viewOurItems.setFont(font)
		self.viewOurItems.setObjectName("viewOurItems")
		#button listener
		self.viewOurItems.clicked.connect(self.openWindow)

		self.viewOurCompanies = QtWidgets.QPushButton(main)
		self.viewOurCompanies.setGeometry(QtCore.QRect(140, 150, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.viewOurCompanies.setFont(font)
		self.viewOurCompanies.setObjectName("viewOurCompanies")
		self.pushButton = QtWidgets.QPushButton(main)
		self.pushButton.setGeometry(QtCore.QRect(170, 200, 201, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.placeAnOrder = QtWidgets.QPushButton(main)
		self.placeAnOrder.setGeometry(QtCore.QRect(180, 260, 181, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.placeAnOrder.setFont(font)
		self.placeAnOrder.setObjectName("placeAnOrder")
		self.pushButton_2 = QtWidgets.QPushButton(main)
		self.pushButton_2.setGeometry(QtCore.QRect(210, 320, 121, 28))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")

		self.retranslateUi(main)
		QtCore.QMetaObject.connectSlotsByName(main)

	def retranslateUi(self, main):
		_translate = QtCore.QCoreApplication.translate
		main.setWindowTitle(_translate("main", "Dialog"))
		self.welcome.setText(_translate("main", "Welcome to Our Market"))
		self.viewOurItems.setText(_translate("main", "View our Items"))
		self.viewOurCompanies.setText(_translate("main", "View Our Companies"))
		self.pushButton.setText(_translate("main", "Sold History"))
		self.placeAnOrder.setText(_translate("main", "Place an Order"))
		self.pushButton_2.setText(_translate("main", "Members"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	main = QtWidgets.QMainWindow()
	ui = Ui_main()
	ui.setupUi(main)
	main.show()
	sys.exit(app.exec_())

