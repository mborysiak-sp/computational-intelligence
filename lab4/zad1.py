import pandas
import numpy

missing_values = ["NA", "-"]

dataframe = pandas.read_csv("iris_with_errors.csv",
                            na_values=missing_values)

print(dataframe.isnull().sum())

for column in dataframe:
    if column != "variety":
        median = dataframe[column].median()
        dataframe[column].fillna(median, inplace=True)
        dataframe[column] = numpy.where((dataframe[column] < 0) & (dataframe[column] > 15),
                                        median,
                                        dataframe[column])

varieties = ["Versicolor",
             "Virginica",
             "Setosa"]

print(dataframe[~dataframe.variety.isin(varieties)])

dataframe["variety"] = numpy.where((dataframe["variety"] == "Versicolour"),
                                   "Versicolor",
                                   dataframe["variety"].str.capitalize())

print(dataframe[~dataframe.variety.isin(varieties)])
