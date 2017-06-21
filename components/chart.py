import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class Chart:
    def __init__(self, iter_num=None, player_num=None):
        self.iter_num = iter_num
        self.player_num = player_num
        self.player_x = []
        self.player_y = []

    def update_head_count(self, x=None, y=None):
        if y is None:
            y = []
        if x is None:
            x = []
        plt.cla()
        plt.title('Head Count')
        plt.xlabel('Iterator')
        plt.ylabel('head count')

        plt.plot(x, y, 'r', label='headcount')

        plt.xlim(1, self.iter_num)
        plt.ylim(0, self.player_num)
        plt.xticks(np.linspace(1, self.iter_num, self.iter_num, endpoint=True))
        plt.yticks(np.linspace(0, self.player_num, self.player_num + 1, endpoint=True))
        plt.legend(bbox_to_anchor=[0.3, 1])
        plt.grid()
        plt.savefig('img/chart_1.jpg', dpi=60)

    def update_capital(self, x=None, y=None):
        if y is None:
            y = []
        if x is None:
            x = []
        plt.cla()
        plt.title('Capital')
        plt.xlabel('Iterator')
        plt.ylabel('capital')

        i = 0
        while i < self.player_num:
            player_x = x[i]
            player_y = y[i]
            plt.plot(player_x, player_y, label=i)
            i += 1

        plt.xlim(1, self.iter_num)
        plt.ylim(0, self.player_num)
        plt.xticks(np.linspace(1, self.iter_num, self.iter_num, endpoint=True))
        plt.yticks(np.linspace(0, self.iter_num, self.iter_num + 1, endpoint=True))
        plt.legend(bbox_to_anchor=[0.3, 1])
        plt.grid()
        # plt.figure(figsize=(5, 2)) 调整图片长宽比例
        plt.savefig('img/chart_2.jpg', dpi=60)
