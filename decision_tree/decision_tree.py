from pandas import read_csv
from sklearn import tree


data = read_csv("data.csv")

data['Color'] = data['Color'].map({'Red': 0, 'Blue': 1})
data['Brand'] = data['Brand'].map({'Snickers': 0, 'Kit Kat': 1})

predictors = ['Color', 'Brand']

X = data[predictors]
Y = data.Class

decisionTreeClassifier = tree.DecisionTreeClassifier(criterion="entropy")
dTree = decisionTreeClassifier.fit(X, Y)

dotData = tree.export_graphviz(dTree, out_file=None)
print(dotData)

print('predict:')
print(dTree.predict([[1, 1]]))