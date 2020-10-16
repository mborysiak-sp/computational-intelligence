"""Knapsack problem - genetic algorithm"""
from pyeasyga.pyeasyga import GeneticAlgorithm


class Item:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


items = [Item("zegar", 100, 7),
         Item("obraz-pejzaz", 300, 7),
         Item("obraz-portret", 200, 6),
         Item("radio", 40, 20),
         Item("laptop", 500, 5),
         Item("lampka nocna", 70, 6),
         Item("srebrne sztucce", 100, 1),
         Item("porcelana", 250, 3),
         Item("figura z brazu", 300, 10),
         Item("skorzana torebka", 280, 3),
         Item("odkurzacz", 300, 15)]


class CustomGeneticAlgorithm(GeneticAlgorithm):
    all_generations = []

    def run(self):
        self.create_first_generation()
        self.all_generations.append(self.current_generation)
        for _ in range(1, self.generations):
            self.create_next_generation()
            self.all_generations.append(self.current_generation)


def fitness(individual, data):
    weight, price = 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            price += item.price
            weight += item.weight
            if weight > 25:
                price = 0
    return price


ga = CustomGeneticAlgorithm(items,
                            population_size=200,
                            generations=100,
                            crossover_probability=0.8,
                            mutation_probability=0.05,
                            elitism=True,
                            maximise_fitness=True)


ga.fitness_function = fitness


def calculate_best_chromosome():
    ga.run()

    return ga.best_individual()


def print_best_chromosome(best_chromosome):
    weight = 0
    for i, item in enumerate(items):
        if best_chromosome[1][i] == 1:
            weight += item.weight
            print(item.name)
    print(f"Total weight: {weight}")
    print(f"Best chromosome: {best_chromosome}")


if __name__ == "__main__":
    best_chromosome_result = calculate_best_chromosome()
    print_best_chromosome(best_chromosome_result)
