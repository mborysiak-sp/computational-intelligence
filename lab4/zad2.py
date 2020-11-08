import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt


df = pd.read_csv("iris.csv")

features = ["sepal.length",
            "sepal.width",
            "petal.length",
            "petal.width"]

x = df.loc[:, features].values
y = df.loc[:, ["variety"]].values

x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data=principalComponents,
                           columns=["principal component 1",
                                    "principal component 2"])

finalDf = pd.concat([principalDf, df[["variety"]]],
                    axis=1)

print(pca.explained_variance_ratio_)
# there's still more than 90 percent of variance after deleting two columns

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)

ax.set_xlabel("Principal component 1", fontsize=15)
ax.set_ylabel("Principal component 2", fontsize=15)
ax.set_title("2 component PCA", fontsize=20)

varieties = ["Setosa",
             "Versicolor",
             "Virginica"]
colors = ["r", "g", "b"]

for variety, color in zip(varieties, colors):
    indicesToKeep = finalDf["variety"] == variety
    ax.scatter(finalDf.loc[indicesToKeep, "principal component 1"],
               finalDf.loc[indicesToKeep, "principal component 2"],
               c=color,
               s=50)

ax.legend(varieties)
ax.grid()
plt.show()
