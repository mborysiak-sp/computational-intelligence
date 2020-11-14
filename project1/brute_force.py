"""Brute force solving of 3-SAT problem"""

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
    formula = Formula("uf20-01.cnf")
    brute_force(formula)
    start_time = time.thread_time()
    end_time = time.thread_time()
    print(end_time - start_time)


if __name__ == "__main__":
    main()
