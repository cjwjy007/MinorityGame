import random

from strategy import Strategy


class Player:
    def __init__(self, memory_num=None, strategy_num=None):
        self.strategy_num = strategy_num
        self.memory_num = memory_num
        self.strategy = Strategy(memory_num=self.memory_num, strategy_num=self.strategy_num)
        self.memory = []
        self._init_random_memory()

    def _init_random_memory(self):
        self.memory = [random.randint(0, 1) for i in range(self.memory_num)]

    def update_memory(self, result=None):
        self.memory.pop(0)
        if result == 1:
            self.memory.append(1)
        else:
            self.memory.append(0)
        self.strategy.update_score(is_win=result)

    def get_strategy_result(self):
        return self.strategy.get_result(self.memory)
