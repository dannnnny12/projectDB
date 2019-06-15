import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import mysql.connector



items_ID = []
items_name = []
produce_time = []
items_price = []
period = []
order_num = []
sold_num = []


class ListViewDemo_items(QWidget):


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

    cursor.execute('SELECT * FROM project.items')
    result = cursor.fetchall()
    print(result)

    for rows in result:
            adjust = list(rows)
            items_ID.append(adjust[0])
            items_name.append(adjust[1])
            produce_time.append(adjust[2])
            items_price.append(adjust[3])
            period.append(adjust[4])
            order_num.append(adjust[5])
            sold_num.append(adjust[6])

    def __init__(self,parent=None):
        super(ListViewDemo_items, self).__init__(parent)

        self.resize(300,270)
        self.setWindowTitle('ITEMS')


        layout=QVBoxLayout()

        listview=QListView()

        slm=QStringListModel()
        self.qList = items_ID
        self.qList1 = items_name
        self.qList2 = produce_time
        self.qList3 = items_price
        self.qList4 = period
        self.qList5 = order_num
        self.qList6 = sold_num

        slm.setStringList(self.qList)

        listview.setModel(slm)

        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,qModelIndex):

        QMessageBox.information(self,'產品資訊',
        '產品名稱:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '公司名稱:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '生產時間:  ' + self.qList2[qModelIndex.row()] + '\n'
        + '產品價格:  ' + self.qList3[qModelIndex.row()] + '\n'
        + '有效期限:  ' + self.qList4[qModelIndex.row()] + '\n'
        + '進貨數量:  ' + self.qList5[qModelIndex.row()] + '\n'
        + '購買數量:  ' + self.qList6[qModelIndex.row()] + '\n')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=ListViewDemo_items()
    win.show()
    sys.exit(app.exec_())
