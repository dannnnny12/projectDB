import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import mysql.connector



sold_num = []
sold_name = []
sold_price = []
sold_amount = []
sold_date = []
menber_num = []


class ListViewDemo_sold(QWidget):


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

    cursor.execute('SELECT * FROM project.itemsold')
    result = cursor.fetchall()
    print(result)

    for rows in result:
            adjust = list(rows)
            sold_num.append(adjust[0])
            sold_name.append(adjust[1])
            sold_price.append(adjust[2])
            sold_amount.append(adjust[3])
            sold_date.append(adjust[4])
            menber_num.append(adjust[5])

    def __init__(self,parent=None):
        super(ListViewDemo_sold, self).__init__(parent)

        self.resize(300,270)
        self.setWindowTitle('SOLD')


        layout=QVBoxLayout()

        listview=QListView()

        slm=QStringListModel()
        self.qList = sold_num
        self.qList1 = sold_name
        self.qList2 = sold_price
        self.qList3 = sold_amount
        self.qList4 = sold_date
        self.qList5 = menber_num

        slm.setStringList(self.qList)

        listview.setModel(slm)

        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,qModelIndex):

        QMessageBox.information(self,'售出資訊',
        '售出編號:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '售出名稱:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '售出價格:  ' + self.qList2[qModelIndex.row()] + '\n'
        + '售出數量:  ' + self.qList3[qModelIndex.row()] + '\n'
        + '售出時間:  ' + self.qList4[qModelIndex.row()] + '\n'
        + '顧客編號:  ' + self.qList5[qModelIndex.row()] + '\n')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=ListViewDemo_sold()
    win.show()
    sys.exit(app.exec_())
