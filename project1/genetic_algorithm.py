import time
from pyeasyga.pyeasyga import GeneticAlgorithm
from matplotlib import pyplot as plt
from project1.formula import Formula


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
