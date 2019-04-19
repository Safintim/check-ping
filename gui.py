# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
# print(resource_path('logo\stim.jpg'))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 624)
        MainWindow.setStyleSheet("font: 12pt \"Bledug\";\n"
"")

        MainWindow.setWindowIcon(QtGui.QIcon(resource_path('logo\stim.jpg')))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
" background: #000;\n"
"\n"
"\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(270, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bledug")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("QPushButton#btn_start{\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    background: #ff8124;\n"
"    cursor: pointer;\n"
"}")
        self.btn_start.setObjectName("btn_start")
        self.btn_select_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select_file.setGeometry(QtCore.QRect(50, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bledug")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_select_file.setFont(font)
        self.btn_select_file.setStyleSheet("QPushButton#btn_select_file{\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    background: #2d2d2d;\n"
"    cursor: pointer;\n"
"}")
        self.btn_select_file.setObjectName("btn_select_file")

        self.stim_logo = QtWidgets.QLabel(self.centralwidget)
        self.stim_logo.setGeometry(QtCore.QRect(170, 5, 171, 41))
        self.pixmap_stim = QtGui.QPixmap(resource_path('logo\stim_logo.png'))
        self.stim_logo.setPixmap(self.pixmap_stim)

        self.iz_logo = QtWidgets.QLabel(self.centralwidget)
        self.iz_logo.setGeometry(QtCore.QRect(170, 556, 171, 41))
        self.pixmap_iz = QtGui.QPixmap(resource_path('logo\iz_logo.png'))
        self.iz_logo.setPixmap(self.pixmap_iz)



        self.label_list_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_list_ip.setGeometry(QtCore.QRect(220, 180, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Bledug")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_list_ip.setFont(font)
        self.label_list_ip.setStyleSheet("QLabel{color: white;}")
        self.label_list_ip.setObjectName("label_list_ip")
        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 140, 391, 21))
        self.line.setStyleSheet("QLineEdit#line{\n"
"color: white;\n"
" background: #2d2d2d;\n"
"\n"
" border-radius: 0px;\n"
"}\n"
"")
        self.line.setObjectName("line")
        self.label_better_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_better_ip.setGeometry(QtCore.QRect(210, 110, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Bledug")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_better_ip.setFont(font)
        self.label_better_ip.setStyleSheet("QLabel{color: white;}\n"
"")
        self.label_better_ip.setObjectName("label_better_ip")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 210, 391, 341))
        self.listView.setStyleSheet("QListWidget#listView{\n"
"color: white;\n"
"font: 15px;\n"
" background: #2d2d2d;\n"
"\n"
" border-radius: 0px;\n"
"}\n"
"")
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Check Ping"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_select_file.setText(_translate("MainWindow", "Select file"))
        self.label_list_ip.setText(_translate("MainWindow", "List IP"))
        self.label_better_ip.setText(_translate("MainWindow", "Better IP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
