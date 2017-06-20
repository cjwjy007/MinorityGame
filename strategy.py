from random import choice
import random

class Strategy:
    def __init__(self, memory_num=None, strategy_num=None):
        self.strategy_num = strategy_num
        self.memory_num = memory_num
        self.strategy_score_dic = {}
        self.current_strategy = None

        # init strategy_score_table
        try:
            random_strategy = random.sample(range(2 ** (2 ** self.memory_num)), self.strategy_num)
            for i in range(len(random_strategy)):
                self.strategy_score_dic[random_strategy[i]] = 0
            self._update_strategy()
        except ValueError as e:
            print(e)
            exit()

    # update current strategy
    def _update_strategy(self):
        max_score = max(self.strategy_score_dic.values())
        max_score_list = [v for i, v in enumerate(self.strategy_score_dic) if self.strategy_score_dic[v] == max_score]
        max_score_index = choice(max_score_list)
        self.current_strategy = max_score_index

    # update the score of current strategy
    def update_score(self, memory=None, cal_sum_flag=None):
        for i in self.strategy_score_dic:
            if self.get_result(memory, i) * cal_sum_flag < 0:
                self.strategy_score_dic[i] += 1
        self._update_strategy()

    # get result from a strategy
    def get_result(self, binary_input: list = None, strategy_input: int = None):
        try:
            if len(binary_input) != self.memory_num:
                raise ValueError('len(input) is not equal to len(memory)')
        except ValueError as e:
            print(e)
            exit()

        input_index = self._bin_to_dec(binary_input)
        strategy_array = self._dec_to_bin(strategy_input)
        return -1 if strategy_array[input_index] == 0 else 1


    # get result from current strategy
    def get_current_strategy_result(self, binary_input: list = None):
        return self.get_result(binary_input, self.current_strategy)

    # bin to dec
    def _bin_to_dec(self, bin_input: list = None):
        dec_sum = 0
        input_len = len(bin_input)
        for idx, val in enumerate(bin_input):
            dec_sum += 2 ** (input_len - idx - 1) * val
        return dec_sum

    # dec to bin
    def _dec_to_bin(self, dec_input: int = None):
        bin_array = []
        while dec_input > 0:
            bin_array.append(dec_input % 2)
            dec_input //= 2
        if len(bin_array) < 2 ** self.memory_num:
            zero_list = [0] * (2 ** self.memory_num - len(bin_array))
            bin_array.extend(zero_list)
        bin_array.reverse()
        return bin_array
