from easydict import EasyDict


class Coins:
    def __init__(self, env):
        self.ENV = env

        colors = env.constant.colors

        self.status = EasyDict({c: 0 for c in colors})
        self.gold = 0

    def env_init(self):
        num = self.ENV.rule.coin.num
        sp = self.ENV.rule.coin.sp

        for k in self.status:
            self.status[k] = num
        self.gold = sp
