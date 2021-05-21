import os
import random
import shutil
import string

import yaml
from easydict import EasyDict

import component.player.move as move
from component.card import Card
from component.hero import Hero


class Env:
    def __init__(self, rule):
        self.utils = Utils
        self.rule = EasyDict(yaml.load(open(os.path.join('rule', rule + '.yaml')), Loader=yaml.FullLoader))
        self.constant = EasyDict({
                'colors': ['black', 'white', 'red', 'blue', 'green'],
                'mid_line': '-' * 100,
                'db_mid_line': '=' * 100,
                'moves': {n: getattr(move, n)() for n in move.Move.choices}
            }
        )

    def start(self):
        random.seed(self.rule.seed)


class Utils:
    @staticmethod
    def generate_cards(env):
        folder = os.path.join('element', env.rule.name, 'cards')
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)
        for _ in range(env.rule.card.num):
            name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            Card.generate(env=env, name=name)

    @staticmethod
    def generate_heroes(env):
        folder = os.path.join('element', env.rule.name, 'heroes')
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)
        for _ in range(env.rule.hero.num):
            name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            Hero.generate(env=env, name=name)
