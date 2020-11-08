import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Zad 1"""

"""a"""
a = 123
b = 321
c = np.multiply(123, 321)
print(f"a: {c}")

"""b"""
a_vector = np.array([3, 8, 9, 10, 12])
b_vector = np.array([8, 7, 7, 5, 6])

sum_vector = a_vector + b_vector
multiply_vector = a_vector * b_vector
print(f"b: sum_vector = {sum_vector}, multiply_vector = {multiply_vector}")

"""c"""
scalar = a_vector.dot(b_vector)
euclidean_distance = np.linalg.norm(a-b)
print(f"c: scalar = {scalar}, euclidean_distance = {euclidean_distance}")

"""d"""
a_matrix = np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]])
b_matrix = np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]])
coordinates_multiply = a_matrix * b_matrix
matrix_multiply = a_matrix.dot(b_matrix)
print(f"d: coordinates_multiply = {coordinates_multiply}, \n matrix_multiply = {matrix_multiply}")

"""e"""
random_vector = np.random.randint(1, 100, 50)
print(f"e: random_vector = {random_vector}")

"""f"""
average = np.average(random_vector)
min_value = np.min(random_vector)
max_value = np.max(random_vector)
standard_deviation = np.std(random_vector)
print(f"f: average = {average}, min_value = {min_value}, max_value = {max_value}, standard_deviation = {standard_deviation}")

"""g"""
normalized_vector = (random_vector - min(random_vector)) / (max(random_vector) - min(random_vector))
max_value_index = np.where(random_vector == np.amax(random_vector))
print(f"g: normalized_vector = {normalized_vector}, max_value_index = {max_value_index}")

"""Zad 2"""

"""a"""
data = pd.read_csv("miasta.csv")
print(f"a: data = {data}")

"""b"""
row = pd.DataFrame([[2010, 460, 555, 405]], columns=data.columns)
data = data.append(row)
print(f"b: data = {data}")

"""c"""
plt.plot(data["Rok"], data["Gdansk"], "g", label="Gdansk")
plt.show()

"""d"""
fig, ax = plt.subplots()
plt.plot(data["Rok"], data["Gdansk"], "g", label="Gdansk")
plt.plot(data["Rok"], data["Szczecin"], "y", label="Szczecin")
plt.plot(data["Rok"], data["Poznan"], "r", label="Poznan")
legend = ax.legend(loc="upper left", fontsize="large")
plt.show()
