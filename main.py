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
            ind1 = random.randint(0, 35)
            ind2 = random.randint(0, 35)
            self.deck[ind1], self.deck[ind2] = self.deck[ind2], self.deck[ind1]

        self.trump = self.deck[0]

    def get(self) -> str:
        ans = 'EMPTY!'

        if self.amount:
            self.amount -= 1
            ans = self.deck.pop(-1)

        return ans

