from easydict import EasyDict

from component.table import Table


class Move:
    choices = [
        "TakeThreeCoinMove",
        "TakeTwoCoinMove",
        "TakeCardMove"
    ]

    def accept(self, player, table, args):
        raise NotImplementedError


class TakeThreeCoinMove(Move):
    def __init__(self):
        self.type = "TakeThreeCoinMove"
        self.require = EasyDict({'card': 0, 'coin': 3})

    def accept(self, player, table, args):
        coins = args.coin
        for coin in coins:
            player.coins.status[coin] += 1
            table.coins.status[coin] -= 1


class TakeTwoCoinMove(Move):
    def __init__(self):
        self.type = "TakeTwoCoinMove"
        self.require = EasyDict({'card': 0, 'coin': 1})

    def accept(self, player, table, args):
        coin = args.coin[0]
        player.coins.status[coin] += 2
        table.coins.status[coin] -= 2


class TakeCardMove(Move):
    def __init__(self):
        self.type = "TakeCardMove"
        self.require = EasyDict({'card': 1, 'coin': 0})

    def accept(self, player, table, args):
        card = args.card
        player.coins.change(card.cost, minus=True)
        player.cards.append(card)
        table.remove_and_update_card_shown(card)



