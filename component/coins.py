from easydict import EasyDict


class Coins:
    def __init__(self, env):
        self.ENV = env

        colors = env.constant.colors
        num = env.rule.coin.num
        sp = env.rule.coin.sp

        self.status = EasyDict({c: num} for c in colors)
        self.special = sp
