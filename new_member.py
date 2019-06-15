import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import mysql.connector



menber_num = []
menber_name = []
gender = []
birthday = []
email = []
menber_address = []


class ListViewDemo_member(QWidget):


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
            menber_num.append(adjust[0])
            menber_name.append(adjust[1])
            gender.append(adjust[2])
            birthday.append(adjust[3])
            email.append(adjust[4])
            menber_address.append(adjust[5])

    def __init__(self,parent=None):
        
        super(ListViewDemo_member, self).__init__(parent)

        self.resize(300,270)
        self.setWindowTitle('MENBER')


        layout=QVBoxLayout()

        listview=QListView()

        slm=QStringListModel()
        self.qList = menber_num
        self.qList1 = menber_name
        self.qList2 = gender
        self.qList3 = birthday
        self.qList4 = email
        self.qList5 = menber_address

        slm.setStringList(self.qList)

        listview.setModel(slm)

        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,qModelIndex):

        QMessageBox.information(self,'顧客資訊',
        '顧客編號:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '顧客姓名:  ' + self.qList1[qModelIndex.row()] + '\n' 
        + '性別:  ' + self.qList2[qModelIndex.row()] + '\n'
        + '生日:  ' + self.qList3[qModelIndex.row()] + '\n'
        + '電子郵件:  ' + self.qList4[qModelIndex.row()] + '\n'
        + '顧客地址:  ' + self.qList5[qModelIndex.row()] + '\n')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=ListViewDemo_member()
    win.show()
    sys.exit(app.exec_())
