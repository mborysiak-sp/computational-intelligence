"""Brute force solving of 3-SAT problem"""
import os
import time
from itertools import product
from project1.formula import Formula
from project1.three_sat import ThreeSAT


def brute_force(formula):
    """
    :param formula: Formula
    :return Tuple containing max found number of solved clauses
    """
    three_sat = ThreeSAT(ga=None, formula=formula)
    all_products = (p for p in product(range(2), repeat=formula.variable_count))
    fitness_value = 0
    for p in all_products:
        fitness_value = three_sat.fitness(p, None)
        if fitness_value == formula.clause_count:
            return fitness_value
    return fitness_value


def main():
    formula = Formula(os.path.join("data", "42_133.cnf"))
    start_time = time.perf_counter()
    best_value = brute_force(formula)
    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time}")
    print(f"Best value: {best_value}")


if __name__ == "__main__":
    main()
