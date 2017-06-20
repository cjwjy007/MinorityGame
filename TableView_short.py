# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableView.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None, player_list=None, player_number=None, memory_number=None):
        self.player_list = player_list
        self.player_number = player_number
        self.memory_number = memory_number
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.tableView.setObjectName("tableView")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(self.memory_number)
        self.tableWidget.setHorizontalHeaderLabels(['Memory'])
        for i in range(self.tableWidget.rowCount()):
            cnt = self.player_list[int(self.player_number)].memory[i]
            newItem = QTableWidgetItem(str(cnt))
            self.tableWidget.setItem(i, 0, newItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
