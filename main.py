from training import test_success_rate, train
from sklearn.neural_network import MLPClassifier


TRAINING_SET_SIZE = 100000
TEST_SET_SIZE = 500


# Docs at
# ANN http://scikit-learn.org/stable/modules/neural_networks_supervised.html#classification
# MLP http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
clf = MLPClassifier(solver='sgd', activation='logistic', hidden_layer_sizes=6, max_iter=100)

train(clf, TRAINING_SET_SIZE)
rate = test_success_rate(clf, TEST_SET_SIZE)

print("Success rate: {0} %".format(round(rate, 2)))
