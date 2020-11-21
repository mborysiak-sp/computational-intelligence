import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split

data = pd.read_csv("iris.csv")

train, test = train_test_split(data,
                               test_size=0.7,
                               stratify=data["variety"])
X_train = train[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y_train = train.variety
X_test = test[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y_test = test.variety
dt = DecisionTreeClassifier(max_depth=3, random_state=1)
dt.fit(X_train, y_train)
r = export_text(dt)
print(r)
prediction = dt.predict(X_test)
print("The accuracy of the Decision Tree is", "{:.3f}".format(metrics.accuracy_score(prediction, y_test)))
plot_tree(dt)
plt.show()
print(confusion_matrix(y_test, prediction))
