# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grep.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 250)
        # 禁止调整窗口大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        # 禁止窗口最大化按钮
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 100, 50))
        self.pushButton.setObjectName("startButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 135, 80, 60))
        self.pushButton_2.setObjectName("searchButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 170, 150, 30))
        self.lineEdit.setObjectName("wordEdit")
        self.lineEdit.setPlaceholderText("请输入关键字，whatsapp")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 150, 30))
        self.lineEdit_2.setObjectName("networtEdit")
        self.lineEdit_2.setPlaceholderText("请输入网络服务名称")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GrepWorld"))
        self.pushButton.setText(_translate("MainWindow", "启动Chrome"))
        self.pushButton_2.setText(_translate("MainWindow", "扫描"))
