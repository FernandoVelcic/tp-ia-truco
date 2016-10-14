import random

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
    ["7 de Basto", "7 de Copa"],
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
        self.identifier = None

    def __str__(self):
        return self.description

    def __repr__(self):
        return self.description + " -> " + str(self.value)

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

    def hand_result(self, card1, card2):
        return card1.compare(card2)

    def result(self):
        hands = zip(*self.cards)
        results = list(map(lambda v: self.hand_result(*v), hands))
        result = sum(i for i in results)

        if results[0] == 0:
            # Caso de parda
            if results[1] == 0:
                if results[2] == 0:
                    return 1
                else:
                    return results[2]
            else:
                return results[1]

        if result == 0:
            return 1
        elif result > 0:
            return 1
        else:
            return -1

    def __repr__(self):
        return str(self.cards)


def to_card(value):
    return lambda description: Card(description, len(cards_order) - value)


cards = flatten(map(to_card(value), card_names) for value, card_names in enumerate(cards_order))


for i, card in enumerate(cards):
    # This is to identify the card with an unique number that well be the input of the neuron
    card.identifier = i


def find_card(matcher):
    for card in cards:
        if matcher(card):
            return card
    raise AssertionError("Could not found card")


def get_card_by_id(identifier):
    return find_card(lambda c: c.identifier == identifier)


def get_card_by_description(description):
    return find_card(lambda c: c.description == description)


def generate_round():
    new_deck = list(cards)
    random.shuffle(new_deck)
    return Round([new_deck[:3], new_deck[3:6]])
