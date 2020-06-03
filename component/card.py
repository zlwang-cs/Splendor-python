import json
import os
import random


class Card:
    def __init__(self, env, path=None):
        self.ENV = env

        if path is not None:
            info = json.load(open(path))
            self.name = info['name']
            self.color = info['color']
            self.point = info['level']
            self.cost = info['cost']
            self.level = info['level']
        else:
            self.name = None
            self.color = None
            self.point = 0
            self.cost = {}
            self.level = -1

    @staticmethod
    def generate(env, name):
        card_dir = os.path.join('element', env.rule.name, 'cards')

        info = {
            'color': random.choice(env.constant.colors),
            'point': random.randint(0, 4),
            'cost': {s: random.randint(0, 3) for s in env.constant.colors},
            'level': random.randint(0, 2)
        }

        with open(os.path.join(card_dir, name + '.card'), 'w') as fout:
            json.dump(info, fout, indent=4)
