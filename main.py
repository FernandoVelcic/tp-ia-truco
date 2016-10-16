from training import test_success_rate, train, exportCSV, importCSV
from sklearn.neural_network import MLPClassifier
import argparse
import ast

parser = argparse.ArgumentParser(description="Truco IA")
parser.add_argument("--export", dest="exportCSV", help="Export a training set to csv")
parser.add_argument("--import", dest="importCSV", help="Import a training set from a csv")
parser.add_argument("--predict", action="store_true", help="Predict mode")
parser.add_argument("--training_set_size", dest="training_set_size", help="Training set size", type=int, default=100000)
parser.add_argument("--test_success_rate", dest="test_set_size", help="Test success rate mode", type=int, default=500)

args = parser.parse_args()

# Docs at
# ANN http://scikit-learn.org/stable/modules/neural_networks_supervised.html#classification
# MLP http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
clf = MLPClassifier(solver="sgd", activation="logistic", hidden_layer_sizes=6, max_iter=100)


if args.exportCSV:
	exportCSV(args.exportCSV, args.training_set_size)

if args.importCSV:
	importCSV(clf, args.importCSV)
else:
	train(clf, args.training_set_size)

if args.predict:
	print("Predict mode. Write exit to exit")
	while True:
		print("Please enter the cards set: ")
		i = input()
		
		if i.strip() == 'exit':
			break

		cards = ast.literal_eval(i)

		if len(cards) != 40:
			print("The array is not valid")
			continue

		result = clf.predict([cards])
		print("Result: " + str(result));
else:
	rate = test_success_rate(clf, args.test_set_size)
	print("Success rate: {0} %".format(round(rate, 2)))
