import pandas
import numpy

missing_values = ["NA", "-"]

dataframe = pandas.read_csv("iris_with_errors.csv",
                            na_values=missing_values)

print(dataframe.isnull().sum())

for column in dataframe:
    if column != "variety":
        dataframe[column] = dataframe[column].where(dataframe[column].between(0, 15),
                                                    numpy.NAN)
        print(dataframe[column].max())
        median = dataframe[column].median()
        dataframe[column].fillna(median, inplace=True)
        print(dataframe[column])

varieties = ["Versicolor",
             "Virginica",
             "Setosa"]

print(dataframe[~dataframe.variety.isin(varieties)])

dataframe["variety"] = dataframe["variety"].str.capitalize()

dataframe["variety"].mask(dataframe["variety"] == "Versicolour", "Versicolor", inplace=True)

print(dataframe[~dataframe.variety.isin(varieties)])
