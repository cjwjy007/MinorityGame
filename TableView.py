# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableView.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None, player_list=None, player_number=None, strategy_number=None):
        self.player_list = player_list
        self.player_number = player_number
        self.strategy_number = strategy_number
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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(self.strategy_number)
        self.tableWidget.setHorizontalHeaderLabels(['Strategy', 'Score'])
        for i in range(self.tableWidget.rowCount()):
            cnt = list(self.player_list[int(self.player_number)].strategy.strategy_score_dic.keys())[i]
            newItem = QTableWidgetItem(str(cnt))
            self.tableWidget.setItem(i, 0, newItem)
        for i in range(self.tableWidget.rowCount()):
            cnt = list(self.player_list[int(self.player_number)].strategy.strategy_score_dic.keys())[i]
            cnt = self.player_list[int(self.player_number)].strategy.strategy_score_dic[cnt]
            newItem = QTableWidgetItem(str(cnt))
            self.tableWidget.setItem(i, 1, newItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
