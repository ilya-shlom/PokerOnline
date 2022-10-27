# This is the beginning of ShulerOnline project

import random


class CardDeck:

    def __init__(self):
        self.amount = 36

        # D - diamonds, H - hearts, C - clubs, S - spades
        # A - 10, B - knave, C - queen, D - king, E - A
        self.deck = [
            'D6', 'D7', 'D8', 'D9', 'DA', 'DB', 'DC', 'DD', 'DE',
            'H6', 'H7', 'H8', 'H9', 'HA', 'HB', 'HC', 'HD', 'HE',
            'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC', 'CD', 'CE',
            'S6', 'S7', 'S8', 'S9', 'SA', 'SB', 'SC', 'SD', 'SE'
        ]

        self.trump = self.deck[0]

    def mix(self):
        for i in range(256):
            ind1 = random.randint(0, self.amount - 1)
            ind2 = random.randint(0, self.amount - 1)
            self.deck[ind1], self.deck[ind2] = self.deck[ind2], self.deck[ind1]

        self.trump = self.deck[0]

    def get(self) -> str:
        ans = ''

        if self.amount:
            self.amount -= 1
            ans = self.deck.pop(-1)

        return ans


class Player:

    def __init__(self):
        # num of cards in player's hand
        self.amount = 0
        # cards in player's hand
        self.hand_deck = []

    def get_card(self, *cards):
        for card in cards:
            self.amount += 1
            self.hand_deck.append(card)

    def put_card(self, cards):
        for card in cards:
            self.amount -= 1
            self.hand_deck.remove(card)

    # aaaaa


pl = Player()
deck = CardDeck()
deck.mix()
for i in range(6):
    pl.get_card(deck.get())
pl.hand_deck.sort()
print(pl.hand_deck)
pl.put_card(input().split())
print(pl.hand_deck)
pl.get_card(*"C9 C8".split())
print(pl.hand_deck)
