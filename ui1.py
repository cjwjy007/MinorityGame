# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from game import Game


class Ui_Form(object):
    def autogame_button_click(self):
        agent = self.lineEdit_agent.text()
        agent_num = int(agent)
        strategies = self.lineEdit_strategies.text()
        str_num = int(strategies)
        memory = self.lineEdit_memory.text()
        memo_len = int(memory)
        iteration = self.lineEdit_iteration.text()
        ite_num = int(iteration)
        new_game = Game(player_num=agent_num, memory_num=memo_len, strategy_num=str_num, iter_num=ite_num)
        new_game.start_game()
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(337, 281)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 141, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(210, 30, 64, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_agent = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_agent.setObjectName("lineEdit_agent")
        self.verticalLayout_3.addWidget(self.lineEdit_agent)
        self.lineEdit_strategies = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_strategies.setObjectName("lineEdit_strategies")
        self.verticalLayout_3.addWidget(self.lineEdit_strategies)
        self.lineEdit_memory = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_memory.setObjectName("lineEdit_memory")
        self.verticalLayout_3.addWidget(self.lineEdit_memory)
        self.lineEdit_iteration = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_iteration.setObjectName("lineEdit_iteration")
        self.verticalLayout_3.addWidget(self.lineEdit_iteration)
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(40, 190, 235, 32))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.human_player = QtWidgets.QPushButton(self.layoutWidget_3)
        self.human_player.setObjectName("human_player")
        self.horizontalLayout.addWidget(self.human_player)
        self.autogame = QtWidgets.QPushButton(self.layoutWidget_3)
        self.autogame.setObjectName("autogame")
        self.horizontalLayout.addWidget(self.autogame)

        self.retranslateUi(Form)
        self.autogame.clicked.connect(self.autogame_button_click)
        self.autogame.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Bar"))
        Form.setWindowIcon(QtGui.QIcon('bar.png'))
        self.label.setText(_translate("Form", "Number of agents"))
        self.label_2.setText(_translate("Form", "Number of strategies"))
        self.label_4.setText(_translate("Form", "Length of memory"))
        self.label_3.setText(_translate("Form", "Number of iterations"))
        self.human_player.setText(_translate("Form", "Human Player"))
        self.autogame.setText(_translate("Form", "AutoGame"))
