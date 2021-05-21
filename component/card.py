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
            self.point = info['point']
            self.cost = info['cost']
            self.level = info['level']
        else:
            self.name = None
            self.color = None
            self.point = 0
            self.cost = {}
            self.level = -1

    def __repr__(self):
        s = f"{self.name}\tpoint: {self.point}\tcost: "
        for k, v in self.cost.items():
            s += f"{k}={v} "
        s += f"\tcolor: {self.color}"
        return s

    def __lt__(self, other):
        return self.name < other.name

    @staticmethod
    def generate(env, name):
        card_dir = os.path.join('element', env.rule.name, 'cards')

        info = {
            'name': name,
            'color': random.choice(env.constant.colors),
            'point': random.randint(0, 4),
            'cost': {s: random.randint(0, 3) for s in env.constant.colors},
            'level': random.randint(0, 2)
        }

        with open(os.path.join(card_dir, name + '.card'), 'w') as fout:
            json.dump(info, fout, indent=4)
