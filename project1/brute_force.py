"""Brute force solving of 3-SAT problem"""
from itertools import product


def brute_force(formula, fitness_function):
    """
    :param fitness_function: method
    :param formula: Formula
    :return Tuple containing max found number of solved clauses
    """
    all_products = (p for p in product(range(2), repeat=formula.variable_count))
    fitness_value = 0
    for p in all_products:
        fitness_value = fitness_function(p, None)
        if fitness_value == formula.clause_count:
            return fitness_value
    return fitness_value
