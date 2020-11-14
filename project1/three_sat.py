"""ThreeSAT logic and functions. Used for both brute force and genetic algorithm"""


class ThreeSAT:
    def __init__(self, formula, ga=None):
        self.ga = ga if ga is not None else None
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
