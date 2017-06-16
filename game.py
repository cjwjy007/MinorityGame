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
            self._notify_players(self._calc_sum())
            print("")

    # calculate sum of player decision
    def _calc_sum(self):
        diff_sum = 0
        for idx, val in enumerate(self.player_list):
            player_strategy = val.get_current_result()
            self.last_result_dic[idx] = player_strategy
            diff_sum += val.get_current_result()
        diff_sum_flag = 1 if diff_sum > 0 else -1
        return diff_sum_flag
        #
        # for i in range(len(self.last_result_dic)):
        #     self.last_result_dic[i] = -1 if self.last_result_dic[i] * diff_sum > 0 else 1

    # tell player the result
    def _notify_players(self, cal_sum_flag=None):
        for idx, val in enumerate(self.player_list):
            val.update_memory(cal_sum_flag)

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
        for player_id, player in enumerate(self.player_list):
            print("player:%d" % player_id, end=' ')
            print("memory:%r" % player.memory, end=' ')
            print("current strategy:%d" % player.strategy.current_strategy, end=' ')
            print("player choice:%d" % player.get_current_result())
            print("strategy table info(s_id:score):", end='')
            for i in player.strategy.strategy_score_dic:
                print("%d:%d" % (i, player.strategy.strategy_score_dic[i]), end=' ')
            print("")
