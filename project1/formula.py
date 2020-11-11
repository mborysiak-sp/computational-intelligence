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
        return any((variable.is_true() for variable in self.variables))


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
