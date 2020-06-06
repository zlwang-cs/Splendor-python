from component.player.player import Player
from component.table import Table


class Move:
    def accept(self, player: Player, table: Table, args):
        raise NotImplementedError


class TakeThreeCoinMove(Move):
    def __init__(self):
        self.type = "TakeThreeCoinMove"

    def accept(self, player, table, coins):
        for coin in coins:
            player.coins.status[coin] += 1
            table.coins.status[coin] -= 1


class TakeTwoCoinMove(Move):
    def __init__(self):
        self.type = "TakeTwoCoinMove"

    def accept(self, player, table, coin):
        player.coins.status[coin] += 2
        table.coins.status[coin] -= 2


class TakeCardMove(Move):
    def __init__(self):
        self.type = "TakeCardMove"

    def accept(self, player, table, card):
        player.cards.append(card)
        table.remove_and_update_card_shown(card)



