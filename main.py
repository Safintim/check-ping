import sys
from check_ping import main
from gui import *
from PyQt5 import QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.file_name = None
                           
        self.ui.btn_select_file.clicked.connect(self.select_file)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.listView.currentItemChanged.connect(self.select_ip)

    def select_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/timur/source','*.txt')[0]

    def remove_all_items_in_listWidget(self):
        while self.ui.listView.takeItem(0):
            self.ui.listView.takeItem(0)

    def start(self):
        
        if self.file_name:
            self.remove_all_items_in_listWidget()
            self.ui.line.text = ''
            ip_list = main(self.file_name)
            self.add_ip_in_list_view(ip_list)
            self.ui.line.setText(ip_list[0])
        else:
            self.error_select_file()
    
    def add_ip_in_list_view(self, ip_list):
        for ip in ip_list:
            ip = QtWidgets.QListWidgetItem(ip)
            self.ui.listView.addItem(ip)
    
    def select_ip(self):
        self.ui.line.setText(self.ui.listView.currentItem().text())
    
    def error_select_file(self):
        reply = QtWidgets.QMessageBox()
        reply.setText("You must select a file")
        reply.exec()    


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
