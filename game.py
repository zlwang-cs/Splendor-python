import argparse
import os

from component.player.player import Player
from component.table import Table
from utils.environ import Env


class Game:
    def __init__(self, rule):
        env = Env(rule=rule)

        env.start()

        env.utils.generate_cards(env)
        env.utils.generate_heroes(env)

        self.ENV = env
        self.table = Table(env)
        self.players = [Player(env)]

    def run(self):
        while True:
            os.system('clear')
            print(self.table)
            for i, player in enumerate(self.players):
                print(f"Player {i}:")
                print("    ", end="")
                print(player)
            print(self.ENV.constant.db_mid_line)
            for i, player in enumerate(self.players):
                print(f"Player {i}:")
                player.move(self.table)
                player.update()
            input("...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rule', dest='rule', default='default', type=str)
    args = parser.parse_args()

    game = Game(args.rule)
    game.run()
