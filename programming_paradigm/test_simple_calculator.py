import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    #tests for addition
    def test_add_positive_numbers(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        result = self.calc.add(5, -4)
        self.assertEqual(result, 1)

    #tests for subtraction
    def test_subtract_positive_numbers(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_subtract_negative_numbers(self):
        result = self.calc.subtract(-10, -5)
        self.assertEqual(result, -5)
    
    def test_subtract_mixed_numbers(self):
        result = self.calc.subtract(-10, 5)
        self.assertEqual(result, -15)
    def test_subtract_result_negative(self):
        result = self.calc.subtract(5, 10)
        self.assertEqual(result, -5)
    
    #test for multiplication
    def test_multiply_positive_numbers(self):
        result = self.calc.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_multiply_negative_numbers(self):
        result = self.calc.multiply(-10, -5)
        self.assertEqual(result, 50)

    def test_multiply_mixed_numbers(self):
        result = self.calc.multiply(10, -5)
        self.assertEqual(result, -50)
    
    def test_multiply_by_zero(self):
        result = self.calc.multiply(10, 0)
        self.assertEqual(result, 0)
    
    #tests for division
    def test_divide_positive_numbers(self):
        result = self.calc.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide_negative_numbers(self):
        result = self.calc.divide(-10, -5)
        self.assertEqual(result, 2)

    def test_divide_mixed_numbers(self):
        result = self.calc.divide(10, -5)
        self.assertEqual(result,-2)

    def test_divide_by_zero(self):
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)

    def test_divide_zero_by_number(self):
        result = self.calc.divide(0, 10)
        self.assertEqual(result, 0)
    
    def test_divide_with_decimal_result(self):
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)

    if __name__ == "__main__":
        unittest.main()



