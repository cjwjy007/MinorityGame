import random

from strategy import Strategy


class Player:
    def __init__(self, memory_num=None, strategy_num=None):
        self.strategy_num = strategy_num
        self.memory_num = memory_num
        self.strategy = Strategy(memory_num=self.memory_num, strategy_num=self.strategy_num)
        self.memory = []
        self.capital = 0
        self._init_random_memory()

    def _init_random_memory(self):
        self.memory = [random.randint(0, 1) for i in range(self.memory_num)]

    # update memory and strategy score
    def update_memory(self, cal_sum_flag=None):
        temp_result = self.get_current_result()
        self.strategy.update_score(memory=self.memory, cal_sum_flag=cal_sum_flag)
        if cal_sum_flag * temp_result == 1:
            self.memory.pop(0)
            self.memory.append(0)
        else:
            self.memory.pop(0)
            self.memory.append(1)
            self.capital = self.capital + 1

    # get strategy result by memory
    def get_current_result(self):
        return self.strategy.get_current_strategy_result(binary_input=self.memory)
