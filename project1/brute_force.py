import time
from itertools import product
from project1.formula import Formula
from project1.three_sat import ThreeSAT


def brute_force(formula):
    three_sat = ThreeSAT(ga=None, formula=formula)
    all_products = (p for p in product(range(2), repeat=formula.variable_count))
    for p in all_products:
        fitness_value = three_sat.fitness(p, None)
        if fitness_value == formula.clause_count:
            print(fitness_value)
            print(p)
            break


def main():
    # formula = Formula("100_403.cnf")
    formula = Formula("uf20-01.cnf")
    tic = time.perf_counter()
    brute_force(formula)
    toc = time.perf_counter()
    print(toc - tic)


if __name__ == "__main__":
    main()
