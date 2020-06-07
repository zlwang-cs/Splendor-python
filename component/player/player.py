from component.coins import Coins
from component.player.decide import InteractiveDecider


class Player:
    def __init__(self, env):
        self.ENV = env

        self.points = 0
        self.power = self.init_power()

        self.cards = []
        self.coins = Coins(env)
        self.heroes = []

        self.decider = InteractiveDecider(env, self)

    def __repr__(self):
        s = f"points: {self.points}\t"
        for k, v in self.power.items():
            s += f"{k}={v} "
        return s

    def init_power(self):
        colors = self.ENV.constant.colors + ['gold']
        return {c: 0 for c in colors}

    def update_power(self):
        pw = self.init_power()
        for c in self.ENV.constant.colors:
            pw[c] += self.coins.status[c]
        for card in self.cards:
            pw[card.color] += 1
        self.power = pw

    def update_points(self):
        points = 0
        for card in self.cards:
            points += card.point
        self.points = points

    def update(self):
        self.update_points()
        self.update_power()

    def move(self, table):
        result = self.decider.decide(table)
        result.move.accept(player=self, table=table, args=result)


