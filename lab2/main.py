"""Knapsack problem - genetic algorithm"""
from pyeasyga.pyeasyga import GeneticAlgorithm
from matplotlib import pyplot as plt


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
    average_fitnesses = []
    best_fitnesses = []

    def run(self):
        self.create_first_generation()
        self.append_generation()
        for _ in range(1, self.generations):
            self.create_next_generation()
            self.append_generation()

    def print_chromosome(self, chromosome):
        weight = 0
        for i, item in enumerate(items):
            if chromosome[1][i] == 1:
                weight += item.weight
                print(item.name)
        print(f"Total weight: {weight}")
        print(f"Best chromosome: {chromosome}")

    def calculate_population_average_fitness(self):
        generation_fitness = [individual.fitness for individual in self.current_generation]
        return sum(generation_fitness) / len(generation_fitness)

    def append_generation(self):
        self.all_generations.append(self.current_generation)
        average_fitness = self.calculate_population_average_fitness()
        self.average_fitnesses.append(average_fitness)
        self.best_fitnesses.append(self.best_individual()[0])

    def calculate_best_chromosome(self):
        self.run()

        return self.best_individual()

    def draw_plots(self):
        fig, ax = plt.subplots()
        plt.plot(self.best_fitnesses, "g", label="Best fitnesses")
        plt.plot(self.average_fitnesses, "y", label="Average fitnesses")
        legend = ax.legend(loc="lower right", fontsize="large")
        plt.show()


def fitness(individual, data):
    weight, price = 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            price += item.price
            weight += item.weight
            if weight > 25:
                price = 0
    return price


if __name__ == "__main__":

    ga = CustomGeneticAlgorithm(items,
                                population_size=200,
                                generations=100,
                                crossover_probability=0.8,
                                mutation_probability=0.05,
                                elitism=True,
                                maximise_fitness=True)

    ga.fitness_function = fitness
    best_chromosome_result = ga.calculate_best_chromosome()
    ga.print_chromosome(best_chromosome_result)
    ga.draw_plots()



