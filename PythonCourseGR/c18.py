import unittest


class Math:

    def __init__(self, operations=None, record=True):
        if isinstance(operations, list):
            self.operations = operations[:]
        else:
            self.operations = list()

        self.record = record

    def sum(self, value1, value2):
        if self.record:
            self.operations.append(("sum", (value1, value2)))
        return value1 + value2

    def difference(self, value1, value2):
        if self.record:
            self.operations.append(("difference", (value1, value2)))
        return value1 - value2

    def multiply(self, value1, value2):
        if self.record:
            self.operations.append(("multiply", (value1, value2)))
        return value1 * value2

    def divide(self, value1, value2):
        if self.record:
            self.operations.append(("divide", (value1, value2)))
        return value1 % value2

    def play(self):
        self.record = False
        for operation in self.operations:
            print(operation[0])
            print(operation[1])
            if hasattr(Math, operation[0]):
                op = getattr(Math, operation[0])
                op(self, *operation[1])


class TestMath(unittest.TestCase):

    def setUpClass(cls) -> None:
        cls.math = Math()
        cls.tests_input = [(1, 0), (0, 1), (1, 2.0), ("1", "2")]

    def test_sum(self):
        # math = Math()
        tests_input = [(1, 0), (0, 1), (1, 2.0), ("1", "2")]
        for inp in self.tests_input:
            result = self.math.sum(*inp)
            print(type(result))
            self.assertIsInstance(result, int)

    def test_sum_001(self):
        # math = Math()
        tests_input = [(1, 0), (0, 1), (1, 2.0), ("1", "2")]
        for inp in self.tests_input:
            result = self.math.divide(*inp)
            print(type(result))
            self.assertIsInstance(result, int)

