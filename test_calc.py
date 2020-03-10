import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):

        calculator = Calc()              # Arrange
        result = calculator.add(10,2)    # ACT
        self.assertEqual(result,12)      # Assert

    def test_subtract(self):

        calculator = Calc()              # Arrange
        result = calculator.subtract(10,2)    # ACT
        self.assertEqual(result,8)      # Assert