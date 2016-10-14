import truco
from sklearn.neural_network import MLPClassifier

round = truco.generate_round()
print(round, round.result())


X = [[3, 2], [1, 6]]
Y = [1, 0]

clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=30,random_state=0)
clf.fit(X, Y)

print(clf.predict([[3., 2.], [1.,3.]]))
print(clf.predict_proba([[3., 2.], [1.,3.]]))
