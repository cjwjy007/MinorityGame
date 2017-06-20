from player import Human, Computer


# player factory
class PlayerFactory:
    def __init__(self, memory_num=None, strategy_num=None):
        self.strategy_num = strategy_num
        self.memory_num = memory_num

    def get_player(self, is_human=None):
        if is_human is True:
            return Human(memory_num=self.memory_num, strategy_num=self.strategy_num)
        elif is_human is False:
            return Computer(memory_num=self.memory_num, strategy_num=self.strategy_num)
