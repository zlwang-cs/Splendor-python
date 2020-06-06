import argparse

from component.player.player import Player
from component.table import Table
from utils.environ import Env


class Game:
    def __init__(self, rule):
        ENV = Env(rule=rule)

        ENV.start()

        ENV.utils.generate_cards(ENV)
        ENV.utils.generate_heroes(ENV)

        self.table = Table(ENV)
        self.players = [Player(ENV)]

    def run(self):
        print(self.table)
        for i, player in enumerate(self.players):
            print(f"Player {i}")
            print("    ", end="")
            print(player)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rule', dest='rule', default='default', type=str)
    args = parser.parse_args()

    game = Game(args.rule)
    game.run()
