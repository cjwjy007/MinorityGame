from game import Game
from PyQt5 import QtWidgets
from ui1 import Ui_Form


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.new = Ui_Form()
        self.new.setupUi(self)


if __name__ == '__main__':
    # new_game = Game(player_num=3, memory_num=3, strategy_num=3, iter_num=100)
    # new_game.start_game()
    # pass
    import sys

    app = QtWidgets.QApplication(sys.argv)
    my_show = MyWindow()
    my_show.show()
    sys.exit(app.exec_())
