from truco import cards, cards_order, generate_round, flatten
import csv


def round_as_training_set(r):
    """
    Transforms the round to the format of the training set with 40 inputs
    :param r:
    :return:
    """
    inputs = list(map(lambda x: 0, range(len(cards))))

    for card in r.player_1_cards():
        inputs[card.identifier] = 1

    for card in r.player_2_cards():
        inputs[card.identifier] = -1

    return inputs


def training_set(n):
    """
    Generates a training set of n quantity of rounds
    :param n: quantity of rounds to generate
    :return: a tuple with the round in training set format (a list of 40 inputs with 1 in the position of the player 1
        cards and -1 in the place of the player 2 cards) and the expected result
    """
    for i in range(n):
        r = generate_round()
        yield round_as_training_set(r), r.result()


def train(clf, n):
    x = list()
    y = list()
    for input_cards, expected_output in training_set(n):
        x.append(input_cards)
        y.append(expected_output)

    clf.fit(x, y)


def exportCSV(filename, n):
    ofile  = open(filename, "w")
    writer = csv.writer(ofile)
    writer.writerow(flatten(cards_order) + ["Result"])
    for input_cards, expected_output in training_set(n):
        writer.writerow(input_cards + [expected_output])
    ofile.close()


def importCSV(clf, filename):
    ifile = open(filename, "r")
    reader = csv.reader(ifile)

    x = list()
    y = list()

    for row in list(reader)[1:]:
        x.append([int(i) for i in row[:40]])
        y.append(int(row[-1]))
    ifile.close()
    
    clf.fit(x, y)


def test_success_rate(clf, n):
    tests_sample = list(map(lambda x: generate_round(), range(n)))
    tests_inputs = list(map(lambda r: round_as_training_set(r), tests_sample))
    real_outputs = list(map(lambda r: r.result(), tests_sample))

    correctly_guessed = 0
    for i, test_case in enumerate(tests_inputs):
        result = clf.predict([test_case])
        if result == real_outputs[i]:
            correctly_guessed += 1

    return (correctly_guessed / n) * 100
