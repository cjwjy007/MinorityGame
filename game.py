from player import Player


class Game:
    def __init__(self, player_num=None, memory_num=None, strategy_num=None, iter_num=None):
        self.iter_num = iter_num
        self.strategy_num = strategy_num
        self.memory_num = memory_num
        self.player_num = player_num
        self._detect_input_error()
        self.player_list = []
        self.last_result_dic = {}
        self._game_init()

    def _game_init(self):
        for i in range(self.player_num):
            self.player_list.append(Player(memory_num=self.memory_num, strategy_num=self.strategy_num))

    # start game
    def start_game(self):
        for i in range(self.iter_num):
            print("this is %dth iteration" % i)
            self._print_current_info()
            self._calc_sum()
            self._notify_players()
            print("")

    # calculate sum of player decision
    def _calc_sum(self):
        diff_sum = 0
        for idx, val in enumerate(self.player_list):
            player_strategy = val.get_strategy_result()
            self.last_result_dic[idx] = player_strategy
            diff_sum += val.get_strategy_result()

        for i in range(len(self.last_result_dic)):
            self.last_result_dic[i] = -1 if self.last_result_dic[i] * diff_sum > 0 else 1

    # tell player the result
    def _notify_players(self):
        for idx, val in enumerate(self.player_list):
            val.update_memory(self.last_result_dic[idx])

    # detect input error
    def _detect_input_error(self):
        # player_num must be odd
        try:
            if self.player_num % 2 == 0:
                raise ValueError('player number must be odd')
        except ValueError as e:
            print(e)
            exit()

    # print information
    def _print_current_info(self):
        for idx, val in enumerate(self.player_list):
            print("player:%d" % idx, end=' ')
            print("memory:%r" % val.memory, end=' ')
            print("current strategy:%d" % val.strategy.current_strategy)
            print("strategy table info(s_id:score):", end='')
            for i in val.strategy.strategy_score_dic:
                print("%d:%d" % (i, val.strategy.strategy_score_dic[i]), end=' ')
            print("")
