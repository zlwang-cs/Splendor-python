import os

from component.card import Card
from component.coins import Coins
from component.hero import Hero


class Table:
    def __init__(self, env):
        self.ENV = env
        self.heroes = self.load_heroes()
        self.cards = self.load_cards()
        self.coins = self.load_coins()

    def load_heroes(self):
        ret = []
        folder = os.path.join('element', self.ENV.rule.name, 'heroes')
        for p in os.listdir(folder):
            path = os.path.join(folder, p)
            ret.append(Hero(env=self.ENV, path=path))
        return ret

    def load_cards(self):
        ret = []
        folder = os.path.join('element', self.ENV.rule.name, 'cards')
        for p in os.listdir(folder):
            path = os.path.join(folder, p)
            ret.append(Card(env=self.ENV, path=path))
        return ret

    def load_coins(self):
        return Coins(self.ENV)
