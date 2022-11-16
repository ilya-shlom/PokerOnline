from classes import *
from cheats import *

table = []
used = []

lobby = Lobby(max_lobby=6, lobby_id=1234, cheats_allowed=False)


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
    while len(player_to_give.hand_deck) < 6 and len(current_deck.cards) > 0:
        player_to_give.get_card(current_deck.get())
    player_to_give.hand_deck.sort()


players = [Player('# 1'), Player('# 2')]

deck = CardDeck()
deck.mix()
tr = deck.trump[0]
tr_card = deck.trump

for p in players:
    for i in range(6):
        p.get_card(deck.get())
    p.hand_deck.sort()

playing_now = 0

print("--------------- SHULER ONLINE ---------------")
print(f'Trump is {tr_card}')



for i in range(len(players)):
    if len(players[i].hand_deck) == 0:
        print(f"Player {i + 1} won!")
print("--------------- SHULER OVER ---------------")
print(
    """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣉⣁⣤⣤⣶⣾⣿⣿⣶⡄⢲⣯⢍⠁⠄⢀⢹⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣿⣿⣏⣉⣹⠿⠇⠄⠽⠿⢷⡈⠿⠇⣀⣻⣿⡿⣻
       ⣿⣿⡿⠿⠛⠛⠛⢛⡃⢉⢣⡤⠤⢄⡶⠂⠄⠐⣀⠄⠄⠄⠄⠄⡦⣿⡿⠛⡇⣼
       ⡿⢫⣤⣦⠄⠂⠄⠄⠄⠄⠄⠄⠄⠄⠠⠺⠿⠙⠋⠄⠄⠄⠢⢄⠄⢿⠇⠂⠧⣿
       ⠁⠄⠈⠁⠄⢀⣀⣀⣀⣀⣠⣤⡤⠴⠖⠒⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢠⡞⠄⣸
       ⡀⠄⠄⠄⠄⠄⠤⠭⠦⠤⠤⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣂⣿
       ⣷⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢳⠄⠄⢀⠈⣠⣤⣤⣼⣿
       ⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣶⣄⡀⠄⠈⠑⢙⣡⣴⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""
)
print("КЧАУ ТЫ ВЫИГРАЛ")
