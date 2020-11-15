"""ThreeSAT logic and functions. Used to call all algorithms"""
import os
from timeit import default_timer as timer

from project1.brute_force import brute_force
from project1.formula import Formula
from project1.genetic_algorithm import CustomGeneticAlgorithm


class ThreeSAT:
    def __init__(self, formula):
        self.formula = formula

    def fitness(self, individual, _):
        """
        :param individual: list of bits
        :param _: None
        :return: integer: score of given individual
        """
        clauses = self.formula.clauses
        score = 0
        for clause in clauses:
            for variable in clause.variables:
                variable.value = individual[variable.index]
            if clause.is_true():
                score = score + 1
        return score

    def test_ga(self):
        """
        Creates CustomGeneticAlgorithm instance and runs it
        :return: tuple(float, int)
        """
        data = [0] * self.formula.variable_count
        clause_count = self.formula.clause_count
        ga = CustomGeneticAlgorithm(data,
                                    clause_count=clause_count,
                                    population_size=100,
                                    generations=200,
                                    crossover_probability=0.8,
                                    mutation_probability=0.1,
                                    elitism=True,
                                    maximise_fitness=True)

        ga.fitness_function = self.fitness

        start_time = timer()
        best_chromosome_result = ga.calculate_best_chromosome()
        end_time = timer()
        time = end_time - start_time
        return time, best_chromosome_result[0]

    def test_brute_force(self):
        """
        Creates CustomGeneticAlgorithm instance and runs it
        :return: tuple(float, int)
        """
        start_time = timer()
        best_result = brute_force(formula=self.formula, fitness_function=self.fitness)
        end_time = timer()
        time = end_time - start_time
        return time, best_result

    def test_algorithms(self):
        """Runs all algorithms and prints their results and times"""
        print("GA: ", self.test_ga())
        print("Brute force: ", self.test_brute_force())


def main():
    formula = Formula(os.path.join("data", "16_18.cnf"))
    three_sat = ThreeSAT(formula=formula)
    three_sat.test_algorithms()


if __name__ == "__main__":
    main()
