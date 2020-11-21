import pandas as pd
import numpy as np


def predict(value):
    if value < 2:
        return 'Setosa'
    elif value < 4.8:
        return 'Versicolor'
    else:
        return 'Virginica'


df = pd.read_csv('iris.csv')
ok = 0
for index in df.values:
    if predict(index[2]) == index[4]:
        ok += 1
print(ok / len(df.values))
print([predict(i[2]) == i[4] for i in df.values].count(True))
print(sum(predict(i[2]) == i[4] for i in df.values))
