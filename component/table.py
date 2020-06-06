import os
import random

from component.card import Card
from component.coins import Coins
from component.hero import Hero


class Table:
    def __init__(self, env):
        self.ENV = env
        self.all_cards = self.load_cards()
        self.all_heroes = self.load_heroes()

        self.heroes = self.init_hero_shown()
        self.coins = self.load_coins()
        self.card_buffer = self.init_card_buffer()
        self.cards = self.init_card_shown()

    def __repr__(self):
        heroes_info = 'Heroes:\n'
        for hero in self.heroes:
            heroes_info += "    " + repr(hero) + "\n"

        cards_info = 'Cards:\n'
        cards_info += "    level 0:\n"
        for i, card in enumerate(self.cards[0]):
            cards_info += "    " + "    " + f"({i}) " + repr(card) + "\n"
        cards_info += "    level 1:\n"
        for i, card in enumerate(self.cards[1]):
            cards_info += "    " + "    " + f"({i}) " + repr(card) + "\n"
        cards_info += "    level 2:\n"
        for i, card in enumerate(self.cards[2]):
            cards_info += "    " + "    " + f"({i}) " + repr(card) + "\n"

        return f"{heroes_info}{self.ENV.constant.mid_line}\n{cards_info}{self.ENV.constant.db_mid_line}"

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

    def init_card_buffer(self):
        ret = [[], [], []]
        for card in self.all_cards:
            level = card.level
            ret[level].append(card)
        random.shuffle(ret[0])
        random.shuffle(ret[1])
        random.shuffle(ret[2])
        return ret

    def init_card_shown(self):
        ret = [[], [], []]
        for l in range(3):
            for _ in range(5):
                ret[l].append(self.card_buffer[l].pop())
        return ret

    def remove_and_update_card_shown(self, card):
        level = card.level
        self.cards[level].remove(card)
        self.cards[level].append(self.card_buffer[level].pop())

    def init_hero_shown(self):
        return sorted(list(random.sample(self.all_heroes, 5)))
