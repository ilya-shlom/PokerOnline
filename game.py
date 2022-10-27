from classes import *


# c_on_t - card on table, inp - player's input
def check_cards(c_on_t, inp):
    if inp[0] == c_on_t[0]:
        return inp[1] > c_on_t[1]
    else:
        return inp[0] == tr


def end_move(current_table, current_used):
    for pair in current_table:
        for card in pair:
            current_used.append(card)
            card.pop()
        pair.pop()


def give_cards(player_to_give, current_deck):
    while len(player_to_give.hand_deck) < 6:
        player_to_give.get_card(current_deck.get())
        if len(current_deck) == 0:
            break


players = [Player('# 1'), Player('# 1')]

deck = CardDeck()
deck.mix()
used = []
tr = deck.trump

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

table = []
playing_now = 0
while players[playing_now].hand_deck > 0 and players[(playing_now + 1) % len(players)].hand_deck > 0:
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



