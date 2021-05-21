import json
import os
import random


class Hero:
    def __init__(self, env, path=None):
        self.ENV = env

        if path is not None:
            info = json.load(open(path))
            self.name = info['name']
            self.point = 3
            self.cost = info['cost']
        else:
            self.name = None
            self.point = 3
            self.cost = {}

    def __repr__(self):
        s = f"{self.name}\tpoint: {self.point}\tcost: "
        for k, v in self.cost.items():
            s += f"{k}={v} "
        return s

    def __lt__(self, other):
        return self.name < other.name

    @staticmethod
    def generate(env, name):
        card_dir = os.path.join('element', env.rule.name, 'heroes')

        info = {
            'name': name,
            'cost': {s: random.randint(0, 3) for s in env.constant.colors},
        }

        with open(os.path.join(card_dir, name + '.hero'), 'w') as fout:
            json.dump(info, fout, indent=4)
