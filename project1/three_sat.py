class ThreeSAT:
    def __init__(self, formula, ga=None):
        self.ga = ga if ga is not None else None
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