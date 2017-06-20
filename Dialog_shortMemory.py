# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_shortMemory.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from TableView_short import Ui_Dialog


class Ui_Dialog_shortMemory(QtWidgets.QDialog):
    def __init__(self, player_list=None, memory_number=None, parent=None):
        self.player_list = player_list
        self.memory_number = memory_number
        super(Ui_Dialog_shortMemory, self).__init__(parent)
        self.setupUi(self)
        self.show()

    def memory_button_click(self):
        player_number = self.lineEdit.text()
        self.Ui_dialog = Ui_Dialog(player_list=self.player_list, player_number=player_number, memory_number=self.memory_number)

    def setupUi(self, Dialog_shortMemory):
        Dialog_shortMemory.setObjectName("Dialog_shortMemory")
        Dialog_shortMemory.resize(386, 158)
        self.label = QtWidgets.QLabel(Dialog_shortMemory)
        self.label.setGeometry(QtCore.QRect(40, 30, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_shortMemory)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 311, 31))
        self.lineEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog_shortMemory)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_shortMemory)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 110, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog_shortMemory)
        self.pushButton.clicked.connect(self.memory_button_click)
        self.pushButton.clicked.connect(Dialog_shortMemory.close)
        self.pushButton_2.clicked.connect(Dialog_shortMemory.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_shortMemory)

    def retranslateUi(self, Dialog_shortMemory):
        _translate = QtCore.QCoreApplication.translate
        Dialog_shortMemory.setWindowTitle(_translate("Dialog_shortMemory", "Memory"))
        self.label.setText(_translate("Dialog_shortMemory", "Input Player Number :"))
        self.pushButton.setText(_translate("Dialog_shortMemory", "OK"))
        self.pushButton_2.setText(_translate("Dialog_shortMemory", "Cancel"))
