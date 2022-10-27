from classes import *

table = []


def put_on_table(c_name, pl):
    pl.putcard(c_name)
    table.append([c_name, ])


players = [Player('# 1'), Player('# 1')]

deck = CardDeck()
deck.mix()

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

print(players[0].hand_deck)
print(players[1].hand_deck)
