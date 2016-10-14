import random

"""
cards_order = [
    ["1E"],
    ["1B"],
    ["7E"],
    ["7O"],
    ["3E", "3O", "3C", "3B"],
    ["2E", "2O", "2C", "2B"],
    ["1O", "1C"],
    ["12E", "12O", "12C", "12B"],
    ["11E", "11O", "11C", "11B"],
    ["10E", "10O", "10C", "10B"],
    ["7O", "7C"],
    ["6E", "6O", "6C", "6B"],
    ["5E", "5O", "5C", "5B"],
    ["4E", "4O", "4C", "4B"],
]
"""

cards_order = [
    ["Ancho de espada"],
    ["Ancho de basto"],
    ["7 de Espada"],
    ["7 de Oro"],
    ["3 de Espada", "3 de Oro", "3 de Copa", "3 de Basto"],
    ["2 de Espada", "2 de Oro", "2 de Copa", "2 de Basto"],
    ["1 de Oro", "1 de Copa"],
    ["12 de Espada", "12 de Oro", "12 de Copa", "12 de Basto"],
    ["11 de Espada", "11 de Oro", "11 de Copa", "11 de Basto"],
    ["10 de Espada", "10 de Oro", "10 de Copa", "10 de Basto"],
    ["7 de Oro", "7 de Copa"],
    ["6 de Espada", "6 de Oro", "6 de Copa", "6 de Basto"],
    ["5 de Espada", "5 de Oro", "5 de Copa", "5 de Basto"],
    ["4 de Espada", "4 de Oro", "4 de Copa", "4 de Basto"],
]


def flatten(l):
    return [item for sublist in l for item in sublist]


class Card:

    def __init__(self, description, value):
        self.description = description
        self.value = value

    def __str__(self):
        return self.description

    def __repr__(self):
        return self.description

    def compare(self, other):
        if not isinstance(other, Card):
            raise TypeError("Cannot compare Card with other thing")
        if self.value > other.value:
            return 1
        elif self.value == other.value:
            return 0
        else:
            return -1


class Round:

    def __init__(self, cards):
        self.cards = cards

    def hand_result(self, hand):
        return hand[0][0].compare(hand[0][1])

    def result(self):
        hands_results = list(map(self.hand_result, 
list(zip(self.cards))))
        if hands_results[0] == 0:
            return hands_results[1]
        else:
            sumed = sum(i for i in hands_results)
            if sumed == 0:
                return 1
            elif sumed > 0:
                return 1
            else:
                return -1

    def __repr__(self):
        return str(self.cards)


cards = flatten([list(map(lambda x: Card(x, len(cards_order) - 
card_value), equal_cards)) for card_value, equal_cards in 
enumerate(cards_order)])


def generate_round():
    new_deck = list(cards)
    random.shuffle(new_deck)
    return Round([new_deck[:3], new_deck[3:6]])