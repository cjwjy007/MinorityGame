# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_longMemory.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from TableView import Ui_Dialog


class Ui_Dialog_longMemory(QtWidgets.QDialog):
    def __init__(self, player_list=None, strategy_number=None, parent=None):
        self.player_list = player_list
        self.strategy_number = strategy_number
        super(Ui_Dialog_longMemory, self).__init__(parent)
        self.setupUi(self)
        self.show()

    def memory_button_click(self):
        player_number = self.lineEdit.text()
        self.Ui_dialog = Ui_Dialog(player_list=self.player_list, player_number=player_number, strategy_number=self.strategy_number)

    def setupUi(self, Dialog_longMemory):
        Dialog_longMemory.setObjectName("Dialog_longMemory")
        Dialog_longMemory.resize(386, 158)
        self.label = QtWidgets.QLabel(Dialog_longMemory)
        self.label.setGeometry(QtCore.QRect(40, 30, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_longMemory)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 311, 31))
        self.lineEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog_longMemory)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_longMemory)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 110, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog_longMemory)
        self.pushButton.clicked.connect(self.memory_button_click)
        self.pushButton.clicked.connect(Dialog_longMemory.close)
        self.pushButton_2.clicked.connect(Dialog_longMemory.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_longMemory)

    def retranslateUi(self, Dialog_longMemory):
        _translate = QtCore.QCoreApplication.translate
        Dialog_longMemory.setWindowTitle(_translate("Dialog_longMemory", "Memory"))
        self.label.setText(_translate("Dialog_longMemory", "Input Player Number :"))
        self.pushButton.setText(_translate("Dialog_longMemory", "OK"))
        self.pushButton_2.setText(_translate("Dialog_longMemory", "Cancel"))
