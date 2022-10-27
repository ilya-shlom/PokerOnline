from classes import *

players = [Player(), Player()]

deck = CardDeck()
deck.mix()
used = []

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

table = []
playing_now = 0
while players[playing_now].hand_deck > 0 and players[1].hand_deck > 0:
    print(players[0].hand_deck)
    print("Choose card: ")
    chosen_card = None
    while not chosen_card:
        chosen_card = input()
        if chosen_card in players[0].hand_deck:
            table.append([chosen_card])
            players[0].put_card(chosen_card)
        else:
            chosen_card = None



