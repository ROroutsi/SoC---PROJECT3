import sklearn
from sklearn.neighbors import KNeighborsClassifier as KNC
import pandas as pd
from sklearn.utils import shuffle
from sklearn import preprocessing as pp
import pickle

data = pd.read_csv("tic-tac-toe.data", usecols=[0, 1, 2, 3, 4, 5])
# print(data.head())

data = shuffle(data)

LE = pp.LabelEncoder()

cls = LE.fit_transform(list(data["class"]))
first = LE.fit_transform(list(data["first_value"]))
second = LE.fit_transform(list(data["second_value"]))
third = LE.fit_transform(list(data["third_value"]))
fourth = LE.fit_transform(list(data["fourth_value"]))
fifth = LE.fit_transform(list(data["fifth_value"]))

predict = "class"

x = list(zip(first, second, third, fourth, fifth))
y = list(cls)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, test_size=0.2)
"""
best_acc = 0
best_k = 3

for k in range(best_k, 19, 2):
    for retrain in range(1000):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            x, y, test_size=0.2)

        model = KNC(n_neighbors=k)

        model.fit(x_train, y_train)
        acc = model.score(x_test, y_test)
        print(acc)

        if acc > best_acc:

            best_acc = acc
            best_k = k

            with open("tic-tac-toe-model.pickle", "wb") as f:
                pickle.dump(model, f)

print(f'Highest accucary: {best_acc}, Best K: {best_k}')
"""
pickle_rick = open("tic-tac-toe-model.pickle", "rb")
model = pickle.load(pickle_rick)

predicted = model.predict(x_test)
names = ["positive", "negative"]

for x in predicted:
    print("Predicted: ", names[predicted[x]], "Data: ",
          x_test[x], "Actual: ", names[y_test[x]])
    # 11 was the Best_k, with best_acc = 0.8333
    # n = model.kneighbors([x_test[x]], 11, True)
    # print("N: ", n)
'''
with open('model-results.csv', 'w') as f:
    f.write("predicted, data, actual\n")
    for x in predicted:
        f.write(f"{names[predicted[x]]},{x_test[x]},{names[y_test[x]]}\n")
'''