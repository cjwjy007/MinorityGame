from components.chart import Chart
from player_factory import PlayerFactory


class Game:
    # singleton
    def __new__(cls, *args, **kw):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def __init__(self, player_num=None, memory_num=None, strategy_num=None, iter_num=None, is_human=None):
        self.is_human = is_human
        self.iter_num = iter_num
        self.strategy_num = strategy_num
        self.memory_num = memory_num
        self.player_num = player_num
        self._detect_input_error()
        self.player_list = []
        self.chart_1_x = []
        self.chart_1_y = []
        self.chart_2_x = []
        self.chart_2_y = []
        self._init_chart_2_xy()
        self.last_result_dic = {}
        self._game_init()
        self.new_chart = Chart(self.iter_num, self.player_num)

    def _game_init(self):
        player_factory = PlayerFactory(memory_num=self.memory_num, strategy_num=self.strategy_num)
        if self.is_human:
            self.player_list.append(player_factory.get_player(is_human=True))
            for i in range(self.player_num - 1):
                self.player_list.append(player_factory.get_player(is_human=False))
        else:
            for i in range(self.player_num):
                self.player_list.append(player_factory.get_player(is_human=False))

    # start game
    def start_game(self,i=None,j=None):
        # for i in range(self.iter_num):
            self.update_chart_1(iter=i)
            self.update_chart_2(iter=i)
            print("this is %dth iteration" % i)
            if self.is_human:
                self.player_list[0].set_current_choice_from_button(j)
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
        if self.is_human:
            human = self.player_list[0]
            print("player:%d" % 0, end=' ')
            print("memory:%r" % human.memory, end=' ')
            print("player choice:%d" % human.get_current_result())
            for player_id, player in enumerate(self.player_list[1:]):
                print("player:%d" % (player_id + 1), end=' ')
                print("memory:%r" % player.memory, end=' ')
                print("current strategy:%d" % player.strategy.current_strategy, end=' ')
                print("player choice:%d" % player.get_current_result())
                print("strategy table info(s_id:score):", end='')
                for i in player.strategy.strategy_score_dic:
                    print("%d:%d" % (i, player.strategy.strategy_score_dic[i]), end=' ')
                print("")
        else:
            for player_id, player in enumerate(self.player_list):
                print("player:%d" % player_id, end=' ')
                print("memory:%r" % player.memory, end=' ')
                print("current strategy:%d" % player.strategy.current_strategy, end=' ')
                print("player choice:%d" % player.get_current_result())
                print("strategy table info(s_id:score):", end='')
                for i in player.strategy.strategy_score_dic:
                    print("%d:%d" % (i, player.strategy.strategy_score_dic[i]), end=' ')
            print("")

            # get head count

    def get_head_count(self):
        head_count = 0
        for player_id, player in enumerate(self.player_list):
            if player.get_current_result() == 1:
                head_count += 1
        return head_count

    def update_chart_1(self, iter):
        self.chart_1_x.append(iter + 1)
        self.chart_1_y.append(self.get_head_count())
        self.new_chart.update_head_count(x=self.chart_1_x, y=self.chart_1_y)

    def _init_chart_2_xy(self):
        self.chart_2_x = [[] for i in range(self.player_num)]
        self.chart_2_y = [[] for i in range(self.player_num)]

    def update_chart_2(self, iter):
        for player_id, player in enumerate(self.player_list):
            self.chart_2_x[player_id].append(iter + 1)
            self.chart_2_y[player_id].append(player.capital)
        self.new_chart.update_capital(x=self.chart_2_x, y=self.chart_2_y)
