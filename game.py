from classes import *

players = [Player(), Player()]

deck = CardDeck()
deck.mix()
used = []

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

print(players[0].hand_deck)
print(players[1].hand_deck)
