from component.player.move import *


class Decider:
    def __init__(self, env, player):
        self.ENV = env
        self.player = player

    def decide(self, table):
        raise NotImplementedError

    @staticmethod
    def generate_result(move, card, coin):
        return EasyDict(move=move, card=card, coin=coin)


class InteractiveDecider(Decider):
    def __init__(self, env, player):
        super().__init__(env, player)

    def decide(self, table):
        for i, m in enumerate(Move.choices):
            print(f"({i}) {m}")
        move_choice = input("Choose an ID: ")
        move_choice = int(move_choice)
        move = self.ENV.constant.moves[Move.choices[move_choice]]
        require = move.require

        card = None
        if require.card == 1:
            card_choice = input("Choose a Card [level(0-2)]+[ID(0-4)]: ")
            card = table.get_card_by_id(card_choice)

        coin = set()
        for i in range(require.coin):
            print(" ".join([f"{i}-{c}" for i, c in enumerate(self.ENV.constant.colors)]))
            coin_choice = int(input("Choose a Coin Color: "))
            coin.add(self.ENV.constant.colors[coin_choice])

        return self.generate_result(move, card, coin)
