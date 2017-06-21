from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QColor

from components.Dialog_longMemory import Ui_Dialog_longMemory
from components.Dialog_shortMemory import Ui_Dialog_shortMemory
from game import Game


class UI_AutoGame(QtWidgets.QMainWindow):
    def __init__(self, player_num=None, memory_num=None, strategy_num=None, iter_num=None, parent=None):
        super(UI_AutoGame, self).__init__(parent)
        self.iter_num = iter_num
        self.strategy_num = strategy_num
        self.memory_num = memory_num
        self.player_num = player_num
        self.label = []
        self.new_game = Game(player_num=self.player_num, memory_num=self.memory_num, strategy_num=self.strategy_num,
                             iter_num=self.iter_num, is_human=False)
        self.total = 0
        self.setupUi(self)
        self.show()

    def view_long_button_click(self):
        self.viewlong = Ui_Dialog_longMemory(self.new_game.player_list, self.strategy_num)

    def view_short_button_click(self):
        self.viewshort = Ui_Dialog_shortMemory(self.new_game.player_list, self.memory_num)

    def continue_button_click(self):
        self.total += 1
        if self.total > self.iter_num:
            return
        self.new_game.start_game(self.total - 1)
        temp = ''
        temp += str(self.total) + '\t\n\n'
        barstate = 0
        for player_id, player in enumerate(self.new_game.player_list):
            barstate += player.get_current_result()
            temp += str(player.get_current_result())
            temp += '\t\n\n'
        if barstate > 0:
            barstate = 1
        else:
            barstate = -1
        temp += str(barstate) + '\t'
        if self.total > 10:
            for i in range(9):
                self.label[i + 1].setText(self.label[i + 2].text())
            self.label[10].setText(temp)
        else:
            self.label[self.total].setText(temp)
        self.label_img1.setPixmap(QPixmap("img/chart_1.jpg"))
        self.label_img1.setAlignment(QtCore.Qt.AlignTop)
        self.label_img2.setPixmap(QPixmap("img/chart_2.jpg"))
        self.label_img2.setAlignment(QtCore.Qt.AlignTop)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 1300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 1100, self.player_num * 40 + 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        temp = 'Round\t\n\n'
        for i in range(self.player_num):
            temp += 'Player_' + str(i) + '\t\n\n'
        temp += 'Bar_State\t'
        self.label.append(QtWidgets.QLabel(temp, self.horizontalLayoutWidget))
        self.label[0].setObjectName("label")
        self.label[0].setGeometry(QtCore.QRect(15, 15, 70, self.player_num * 40 + 20))
        self.label[0].setMaximumSize(QtCore.QSize(70, self.player_num * 40 + 20))
        self.label[0].setMinimumSize(QtCore.QSize(70, self.player_num * 40 + 20))
        self.horizontalLayout.addWidget(self.label[0], 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        for i in range(10):
            self.label.append(QtWidgets.QLabel(self.horizontalLayoutWidget))
            self.label[i + 1].setGeometry(QtCore.QRect(15 + (i + 1) * 70, 30, 70, self.player_num * 40 + 20))
            self.label[i + 1].setMaximumSize(QtCore.QSize(70, self.player_num * 40 + 20))
            self.label[i + 1].setMinimumSize(QtCore.QSize(70, self.player_num * 40 + 20))
            self.label[i + 1].setObjectName("label" + str(i))
            self.horizontalLayout.addWidget(self.label[i + 1], 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.contin = QtWidgets.QPushButton('continue', self.centralwidget)
        self.contin.setGeometry(QtCore.QRect(20, self.player_num * 40 + 35, 130, 20))
        self.contin.setObjectName("continue")
        self.contin.clicked.connect(self.continue_button_click)

        self.view_short = QtWidgets.QPushButton('View Short Memory', self.centralwidget)
        self.view_short.setGeometry(QtCore.QRect(160, self.player_num * 40 + 35, 130, 20))
        self.view_short.setObjectName("view_short")
        self.view_short.clicked.connect(self.view_short_button_click)

        self.view_long = QtWidgets.QPushButton('View Long Memory', self.centralwidget)
        self.view_long.setGeometry(QtCore.QRect(300, self.player_num * 40 + 35, 130, 20))
        self.view_long.setObjectName("view_long")
        self.view_long.clicked.connect(self.view_long_button_click)

        self.label_img1 = QtWidgets.QLabel(self.centralwidget)
        self.label_img1.setGeometry(QtCore.QRect(20, self.player_num * 40 + 60, 600, 600))
        self.label_img1.setObjectName("label_img1")

        self.label_img2 = QtWidgets.QLabel(self.centralwidget)
        self.label_img2.setGeometry(QtCore.QRect(525, self.player_num * 40 + 60, 600, 600))
        self.label_img1.setObjectName("label_img2")

        palette1 = QtGui.QPalette()
        palette1.setColor(self.backgroundRole(), QColor('#FFF5EE'))  # 设置背景颜色
        # palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('img/background.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.setAutoFillBackground(True)

        '''self.contin1 = QtWidgets.QPushButton('continue', self.centralwidget)
        self.contin1.setGeometry(QtCore.QRect(20,self.player_num*40+100, 100,30 ))
        self.contin1.setObjectName("pushButton1")
        self.contin1.clicked.connect(self.continue_button_click)'''

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
