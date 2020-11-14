"""Formula related logic. Formula contains clauses which contain variables"""


def is_int(string):
    """
    :param string: str
    :return: Boolean. True for string containing a digit, even for negative ones.
    """
    return string.lstrip("-+").isdigit()


def get_integers_from_string(string):
    """
    :param string: str
    :return: List of integers extracted from given string
    """
    # Rstrip removes \n from every line and split returns words out of it
    words = string.rstrip().split(" ")
    integers = [int(word) for word in words if is_int(word) and int(word) != 0]
    return integers


class Variable:
    """Class with logic related to variable"""
    def __init__(self, unprocessed_variable):
        unprocessed_variable_int = int(unprocessed_variable)
        # values from file start from 1 instead of 0
        self.index = abs(unprocessed_variable_int) - 1
        self.is_negative = unprocessed_variable_int < 0
        self.value = None

    def is_true(self):
        """
        :return: Boolean. True if variable's value is true or if false and negated
        """
        if self.is_negative:
            return not self.value
        return self.value


class Clause:
    """Class with logic related to clause. Clause contains three variables"""
    def __init__(self, line):
        self.variables = []
        self.read_clause(line)

    def read_clause(self, line):
        """
        Extracts variables' values from given string and appends Variable objects to itself
        :param line: str
        """
        unprocessed_variables = get_integers_from_string(line)
        for unprocessed_variable in unprocessed_variables:
            self.variables.append(Variable(unprocessed_variable))

    def is_true(self):
        """
        :return: Boolean. True if all variables in the clause are returning True.
        """
        return any((variable.is_true() for variable in self.variables))


class Formula:
    """Class with formula logic. Stores a list of clauses, their length and number of total extracted variables"""
    def __init__(self, dimacs_file_name):
        self.clauses = []
        self.clause_count = 0
        self.variable_count = 0
        self.read_dimacs(dimacs_file_name)

    def read_dimacs(self, dimacs_file_name):
        """
        Opens a dimacs format file and extracts 3-SAT related values from it.
        :param dimacs_file_name: str
        """
        with open(dimacs_file_name) as dimacs_file:
            lines = dimacs_file.readlines()
            header = [line for line in lines if line.startswith("p")][0]
            lines_with_clauses = [line for line in lines if line.startswith(("c", "p")) is False]
            self.extract_clauses(lines_with_clauses)
            self.extract_counts(header)

    def extract_counts(self, header):
        """
        Extracts values from header of dimacs file
        :param header: str
        """
        self.variable_count, self.clause_count = get_integers_from_string(header)

    def extract_clauses(self, lines_with_clauses):
        """
        Creates a list of objects of Clause type from given list
        :param lines_with_clauses: list of strings
        """
        for line in lines_with_clauses:
            self.clauses.append(Clause(line))
