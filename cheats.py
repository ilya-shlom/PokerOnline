from classes import *

sure_deck = []


# us - used, h_d - hand_deck, tab - table
def prob_deck_build(us, h_d, tr, tab=None):
    if tab is None:
        tab = []
    deck = CardDeck()
    prob_deck = deck.deck
    prob_deck.remove(tr)
    for card in h_d:
        prob_deck.remove(card)
    for card in us:
        prob_deck.remove(card)
    for card in tab:
        prob_deck.remove(card)
    return prob_deck


def sure_deck_build(tab):
    for pairs in tab:
        for card in pairs:
            sure_deck.append(card)


