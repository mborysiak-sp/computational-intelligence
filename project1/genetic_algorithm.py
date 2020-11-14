"""Genetic algorithm implementation"""
from pyeasyga.pyeasyga import GeneticAlgorithm
from matplotlib import pyplot as plt


class CustomGeneticAlgorithm(GeneticAlgorithm):
    """Extended version of pyeasyga GeneticAlgorithm class"""
    all_generations = []
    average_fitnesses = []
    best_fitnesses = []

    def __init__(self, *args, clause_count, **kwargs):
        super().__init__(*args, **kwargs)
        self.clause_count = clause_count

    def run(self):
        """Extends inherited run() method with additional check for searched value"""
        self.create_first_generation()
        self.append_generation()
        for _ in range(1, self.generations):
            self.create_next_generation()
            self.append_generation()
            # Check if current best individual is equal to searched number of true clauses and break loop if True
            if self.best_individual()[0] == self.clause_count:
                break

    def calculate_population_average_fitness(self):
        """
        Calculates average fitness of currently stored generation
        :return integer"""
        generation_fitness = [individual.fitness for individual in self.current_generation]
        return sum(generation_fitness) / len(generation_fitness)

    def append_generation(self):
        """Appends currently stored generation to list of generations"""
        self.all_generations.append(self.current_generation)
        average_fitness = self.calculate_population_average_fitness()
        self.average_fitnesses.append(average_fitness)
        self.best_fitnesses.append(self.best_individual()[0])

    def calculate_best_chromosome(self):
        """Runs run method and returns best individual found"""
        self.run()
        return self.best_individual()

    def draw_plots(self):
        """Draws plots for best and average fitness of algorithm"""
        fig, ax = plt.subplots()
        plt.plot(self.best_fitnesses, "g", label="Best fitness")
        plt.plot(self.average_fitnesses, "y", label="Average fitness")
        ax.legend(loc="lower right", fontsize="large")
        plt.show()
