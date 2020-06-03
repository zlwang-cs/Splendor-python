import os
import random
import shutil
import string

from component.card import Card
from component.hero import Hero


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
