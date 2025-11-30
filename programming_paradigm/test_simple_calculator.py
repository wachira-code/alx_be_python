import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    #tests for addition
    def test_addition(self):
        self.assertEqual(self.calc.add(5,2), 7)
        self.assertEqual(self.calc.add(-5, 2), 3)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.6), 6.1)
        self.assertEqual(self.calc.add(-5,-2), -7)

    #tests for subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3)
        self.assertEqual(self.calc.subtract(-5, -5), -10)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    #test for multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(5, -6), -30)
        self.assertEqual(self.calc.multiply(-5, -6), 30)
        self.assertEqual(self.calc.multiply(5, 0), 0)
    
    #tests for division
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, -5,), -2)
        self.assertEqual(self.calc.divide(-10, -5), 2)
        self.assertEqual(self.calc.divide(10, 2.5), 4)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    if __name__ == "__main__":
        unittest.main()



