from render import ConsoleRenderer
from bot import Durak, DECK
import random
import time


def local_game():
    # rng = random.Random(42)  # игра с фиксированным рандомом (для отладки)
    rng = random.Random()  # случайная игра
    turn = 0
    card_appearance = dict.fromkeys(DECK)
    for card in tuple(card_appearance.keys()):
        card_appearance.update({card: [None, None, None]})

    my_index = 0
    g = Durak(rng=rng)
    renderer = ConsoleRenderer()

    renderer.help()

    while not g.winner:
        # print(f'Ход {turn}')
        renderer.render_game(g, my_index=0)

        renderer.sep()
        for p in range(2):
            for card_from_hand in g.players[p].cards:
                if card_appearance[card_from_hand] == [None, None, None]:
                    card_appearance[card_from_hand][0] = turn
                    card_appearance[card_from_hand][1] = turn
                    card_appearance[card_from_hand][2] = p
                else:
                    card_appearance[card_from_hand][1] = turn
        my_index, choice = g.simple_algorithm(my_index)
        # print(choice)
        # разбиваем на части: команда - пробел - номер карты
        parts = choice.lower().split(' ')
        if not parts:
            break

        command = parts[0]

        try:
            if command == 'f':
                r = g.finish_turn()
                # print(f'Ход окончен: {r}')
                turn += 1
            elif command == 'a':
                index = int(parts[1]) - 1
                card = g.attacking_player[index]
                if not g.attack(card):
                    pass
                    # print('Вы не можете ходить с этой карты!')
            elif command == 'd':
                index = int(parts[1]) - 1
                new_card = g.defending_player[index]
                    # with open(f'game_logs/{new_card[0]}_throw.csv', 'a') as data:
                    #     data.write(f'{turn};')


                # варианты защиты выбранной картой
                variants = g.defend_variants(new_card)

                if len(variants) == 1:
                    def_index = 0

                else:
                    def_index = int(input(f'Какую позицию отбить {new_card}? ')) - 1

                old_card = list(g.field.keys())[def_index]
                if not g.defend(old_card, new_card):
                    pass
                    # print('Не можете так отбиться')
            elif command == 'q':
                for card_final in DECK:
                    if card_final[1] != g.trump_suit:
                        with open(f'game_logs/{card_final[0]}.csv', 'a') as data:
                            res = 1 if len(g.players[card_appearance[card_final][2]].cards) == 0 else 0
                            data.write(f'{card_appearance[card_final][1] - card_appearance[card_final][0]};{res};\n')
                    else:
                        with open(f'game_logs/{card_final[0]}_trump.csv', 'a') as data:
                            res = 1 if len(g.players[card_appearance[card_final][2]].cards) == 0 else 0
                            data.write(f'{card_appearance[card_final][1] - card_appearance[card_final][0]};{res};\n')
                # print(card_appearance)
                # print('QUIT!')
                break
        except IndexError:
            pass
            # print('Неправильный выбор карты')
        except ValueError:
            pass
            # print('Введите число через пробел после команды')

        if g.winner:
            # print(f'Игра окончена, победитель игрок: #{g.winner + 1}')
            break
        # time.sleep(1)


if __name__ == '__main__':
    for i in range(1000000):
        local_game()
