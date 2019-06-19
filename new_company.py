import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import mysql.connector

company_ID = []
company_name = []


class ListViewDemo_companies(QWidget):

    def divide_element(input_ele, num):
        for rows in input_ele:
            adjust = list(rows)
            input_ele.append(adjust[num])
        return input_ele

    db_connect = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'abit850923',
        database = '',
    )

    cursor = db_connect.cursor()

    cursor.execute('SELECT * FROM project.company')
    result = cursor.fetchall()
    print(result)

    for rows in result:
        adjust = list(rows)
        company_ID.append(adjust[0])
        company_name.append(adjust[1])



    def __init__(self,parent=None):
        super(ListViewDemo_companies, self).__init__(parent)

        self.resize(300,270)
        self.setWindowTitle('COMPANY')


        layout=QVBoxLayout()

        listview=QListView()

        slm=QStringListModel()
        self.qList = company_ID
        self.qList1 = company_name

        slm.setStringList(self.qList)

        listview.setModel(slm)

        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,qModelIndex):

        QMessageBox.information(self,'公司資訊',
        '公司名稱:'+self.qList1[qModelIndex.row()])

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=ListViewDemo_companies()
    win.show()
    sys.exit(app.exec_())
