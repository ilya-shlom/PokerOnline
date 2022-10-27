from classes import *


# c_on_t - card on table, inp - player's input
def check_cards(c_on_t, inp):
    if inp[0] == c_on_t[0]:
        if inp[1] > c_on_t[1]:
            return True
        else:
            return False
    elif inp[0] == tr:
        return True
    else:
        return False


players = [Player(), Player()]

deck = CardDeck()
deck.mix()
tr = deck.trump

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

print(players[0].hand_deck)
print(players[1].hand_deck)
