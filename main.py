import argparse

from utils.environ import Env
from utils.utils import Utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rule', dest='rule', default='default', type=str)
    args = parser.parse_args()
    ENV = Env(rule=args.rule)

    ENV.start()

    Utils.generate_cards(ENV)
    Utils.generate_heroes(ENV)


