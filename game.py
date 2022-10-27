from classes import *


table = []
used = []


def put_on_table(c_name, pl):
    pl.put_card(c_name)
    table.append([c_name, ])


# c_on_t - card on table, inp - player's input
def check_card(c_on_t, inp):
    if inp[0] == c_on_t[0]:
        return inp[1] > c_on_t[1]
    else:
        return inp[0] == tr


# c_on_t - card on table, inp - player's input, pl - current player
def cover_card(c_on_t, inp, pl):
    if check_card(c_on_t, inp):
        table[-1].append(inp)
        pl.put_card(inp)
    else:
        print("Choose another card!")


# c_on_t - card on table, inp - player's input, pl - current player
def get_from_table(pl):
    pl.get_card(*table.pop())


def end_move():
    for pair in table:
        while len(pair) != 0:
            used.append(pair.pop())
        table.pop()


def give_cards(player_to_give, current_deck):
    while len(player_to_give.hand_deck) < 6 and len(current_deck.deck) > 0:
        player_to_give.get_card(current_deck.get())
    player_to_give.hand_deck.sort()


players = [Player('# 1'), Player('# 2'), Player('# 3'), Player('# 4')]

deck = CardDeck()
deck.mix()
tr = deck.trump

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

playing_now = 0

print("--------------- SHULER ONLINE ---------------")
print(f'Trump is {tr}')
while len(players[playing_now].hand_deck) > 0 and len(players[abs((playing_now - 1)) % len(players)].hand_deck) > 0:
    print(f'New Round: Player {playing_now + 1}')
    # 1st player
    print(players[playing_now].hand_deck)
    chosen_card = None
    while not chosen_card:
        print("Choose card: ", end='')
        chosen_card = input()
        if chosen_card in players[playing_now].hand_deck:
            put_on_table(chosen_card, players[playing_now])
            print(f"Table: {table}")
        else:
            print("Input Error! Choose another card.")
            chosen_card = None

    # 2nd player
    print(players[(playing_now+1) % len(players)].hand_deck)
    chosen_card = None
    while not chosen_card:
        print("Choose card from deck or take cards by TAKE: ", end='')
        chosen_card = input()
        if chosen_card in players[(playing_now+1) % len(players)].hand_deck\
                and check_card(table[len(table)-1][0], chosen_card):
            cover_card(table[len(table)-1][0], chosen_card, players[(playing_now+1) % len(players)])
            print(f"Table: {table}")
            end_move()
            playing_now = (playing_now + 1) % len(players)
        elif chosen_card == "TAKE":
            get_from_table(players[(playing_now+1) % len(players)])
            print(players[(playing_now + 1) % len(players)].hand_deck)
            playing_now = (playing_now + 2) % len(players)
        else:
            print("Input Error! Choose another card.")
            chosen_card = None

    for i in range(len(players)):
        give_cards(players[(playing_now + i) % len(players)], deck)

    print(f'Used cards: {used}')
    print()

for i in range(len(players)):
    if len(players[i].hand_deck) == 0:
        print(f"Player {i+1} won!")
print("--------------- SHULER OVER ---------------")
