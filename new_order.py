import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import mysql.connector



order_num = []
pay_method = []
import_num = []
company_ID = []



class ListViewDemo_order(QWidget):


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

    cursor.execute('SELECT * FROM project.members')
    result = cursor.fetchall()
    print(result)

    for rows in result:
            adjust = list(rows)
            order_num.append(adjust[0])
            pay_method.append(adjust[1])
            import_num.append(adjust[2])
            company_ID.append(adjust[3])
            

    def __init__(self,parent=None):
        super(ListViewDemo_order, self).__init__(parent)

        self.resize(150,75)
        self.setWindowTitle('ORDER')


        layout=QVBoxLayout()

        listview=QListView()

        slm=QStringListModel()
        self.qList = order_num
        self.qList1 = pay_method
        self.qList2 = import_num
        self.qList3 = company_ID

        slm.setStringList(self.qList)

        listview.setModel(slm)

        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,qModelIndex):

        QMessageBox.information(self,'訂單資訊',
        '訂單編號:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '付款方式:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '付款金額:  ' + self.qList2[qModelIndex.row()] + '\n'
        + '公司編號:  ' + self.qList3[qModelIndex.row()] + '\n')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=ListViewDemo_order()
    win.show()
    sys.exit(app.exec_())
