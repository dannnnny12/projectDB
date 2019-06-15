# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from new_item import ListViewDemo_items
from new_company import ListViewDemo_companies
from new_sold import ListViewDemo_sold
from new_member import ListViewDemo_member
from new_order import ListViewDemo_order
class Ui_main(object):
	def openItemsWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui= ListViewDemo_items()
		self.ui.__init__(self.window)
		self.window.show()

	def openCompanyWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui= ListViewDemo_companies()
		self.ui.__init__(self.window)
		self.window.show()

	def openSoldWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui= ListViewDemo_sold()
		self.ui.__init__(self.window)
		self.window.show()

	def openOrderWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui= ListViewDemo_order()
		self.ui.__init__(self.window)
		self.window.show()

	def openMemberWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui= ListViewDemo_member()
		self.ui.__init__(self.window)
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
		self.viewOurItems.clicked.connect(self.openItemsWindow)

		self.viewOurCompanies = QtWidgets.QPushButton(main)
		self.viewOurCompanies.setGeometry(QtCore.QRect(140, 150, 241, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.viewOurCompanies.setFont(font)
		self.viewOurCompanies.setObjectName("viewOurCompanies")

		self.viewOurCompanies.clicked.connect(self.openCompanyWindow)

		self.pushButton = QtWidgets.QPushButton(main)
		self.pushButton.setGeometry(QtCore.QRect(170, 200, 201, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.openSoldWindow)


		self.placeAnOrder = QtWidgets.QPushButton(main)
		self.placeAnOrder.setGeometry(QtCore.QRect(180, 260, 181, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.placeAnOrder.setFont(font)
		self.placeAnOrder.setObjectName("placeAnOrder")
		self.placeAnOrder.clicked.connect(self.openOrderWindow)



		self.pushButton_2 = QtWidgets.QPushButton(main)
		self.pushButton_2.setGeometry(QtCore.QRect(210, 320, 121, 28))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_2.clicked.connect(self.openMemberWindow)

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
	
