from pyeasyga.pyeasyga import GeneticAlgorithm
from matplotlib import pyplot as plt


def is_int(string):
    return string.lstrip("-+").isdigit()


class Clause:
    variables = []

    def __init__(self, line):
        self.read_clause(line)

    def read_clause(self, line):
        line = line.split(" ")
        variables = [value for value in line if is_int(value)]
        self.variables = variables


class Formula:
    clauses = []
    clause_count = 0
    variable_count = 0

    def __init__(self, dimacs_file_name):
        self.read_dimacs(dimacs_file_name)

    def read_dimacs(self, dimacs_file_name):
        with open(dimacs_file_name) as dimacs_file:
            lines = dimacs_file.readlines()
            header = [line for line in lines if line.startswith("p")]
            self.variable_count, self.clause_count = [word for word in header if is_int(word)]
            lines_with_clauses = [line for line in lines if line.startswith(("c", "p")) is False]
            for line in lines_with_clauses:
                self.clauses.append(Clause(line))


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


def main():
    formula = Formula("CBS_k3_n100_m403_b10_0.cnf")


if __name__ == "__main__":
    main()

