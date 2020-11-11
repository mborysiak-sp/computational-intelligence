import time
from pyeasyga.pyeasyga import GeneticAlgorithm
from matplotlib import pyplot as plt


def is_int(string):
    return string.lstrip("-+").isdigit()


def get_integers_from_string(string):
    # Rstrip removes \n from every line and split returns words out of it
    words = string.rstrip().split(" ")
    integers = [int(word) for word in words if is_int(word) and int(word) != 0]
    return integers


class Variable:
    def __init__(self, unprocessed_variable):
        unprocessed_variable_int = int(unprocessed_variable)
        # values from file start from 1 instead of 0
        self.index = abs(unprocessed_variable_int) - 1
        self.is_negative = unprocessed_variable_int < 0
        self.value = None

    def is_true(self):
        if self.is_negative:
            return not self.value
        return self.value


class Clause:
    def __init__(self, line):
        self.variables = []
        self.read_clause(line)

    def read_clause(self, line):
        unprocessed_variables = get_integers_from_string(line)
        for unprocessed_variable in unprocessed_variables:
            self.variables.append(Variable(unprocessed_variable))

    def is_true(self):
        return any([variable.is_true() for variable in self.variables])


class Formula:
    def __init__(self, dimacs_file_name):
        self.clauses = []
        self.clause_count = 0
        self.variable_count = 0
        self.read_dimacs(dimacs_file_name)

    def read_dimacs(self, dimacs_file_name):
        with open(dimacs_file_name) as dimacs_file:
            lines = dimacs_file.readlines()
            header = [line for line in lines if line.startswith("p")][0]
            lines_with_clauses = [line for line in lines if line.startswith(("c", "p")) is False]
            self.extract_clauses(lines_with_clauses)
            self.extract_counts(header)

    def extract_counts(self, header):
        self.variable_count, self.clause_count = get_integers_from_string(header)

    def extract_clauses(self, lines_with_clauses):
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


class ThreeSAT:
    def __init__(self, ga, formula):
        self.ga = ga
        self.formula = formula

    def fitness(self, individual, _):
        clauses = self.formula.clauses
        score = 0
        for clause in clauses:
            for variable in clause.variables:
                variable.value = individual[variable.index]
            if clause.is_true():
                score = score + 1
        return score


def main():
    # formula = Formula("CBS_k3_n100_m403_b10_0.cnf")
    formula = Formula("250_1065.cnf")
    data = [0] * formula.variable_count
    ga = CustomGeneticAlgorithm(data,
                                population_size=100,
                                generations=100,
                                crossover_probability=0.8,
                                mutation_probability=0.5,
                                elitism=True,
                                maximise_fitness=True)
    three_sat = ThreeSAT(ga=ga, formula=formula)
    three_sat.ga.fitness_function = three_sat.fitness
    tic = time.perf_counter()
    best_chromosome_result = three_sat.ga.calculate_best_chromosome()
    toc = time.perf_counter()
    print(toc - tic)
    print(best_chromosome_result)
    three_sat.ga.draw_plots()


if __name__ == "__main__":
    main()
