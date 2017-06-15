from random import choice, random


class strategy:
    def __init__(self, memory=None, strategy_num=None):
        self.strategy_num = strategy_num
        self.memory = memory
        self.strategy_score_list = {}
        self.current_strategy = None

        # init strategy_score_table
        for i in range(self.strategy_num):
            random.sample(range(2 ** (2 ** memory)), 5)
            self.strategy_score_list.append(0)

    def select_strategy(self):
        max_score = max(self.strategy_score_list)
        max_score_list = [i for i, v in enumerate(self.strategy_score_list) if v == max_score]
        max_score_index = choice(max_score_list)
        self.current_strategy = max_score_index

    def get_result(self, binary_input=None):
        index = self.binary_input_to_index(binary_input)

        pass

    def binary_input_to_index(self,binary_input=None):
        index_sum = 0
        for idx,val in enumerate(binary_input):
            index_sum += 10**idx * val
        return index_sum

