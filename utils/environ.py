import os
import random

import yaml
from easydict import EasyDict


class Env:
    def __init__(self, rule):
        self.rule = EasyDict(yaml.load(open(os.path.join('rule', rule + '.yaml')), Loader=yaml.FullLoader))
        self.constant = EasyDict({
                'colors': ['black', 'white', 'red', 'blue', 'green']
            }
        )

    def start(self):
        random.seed(self.rule.seed)
