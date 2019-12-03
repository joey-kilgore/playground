import unittest
import calc

class TestCalc(unittest.TestCase):
    # Note that the naming convention test_<func> MUST be followed   
    def test_add(self):
        self.assertEqual(calc.add(1,2), 3)
        self.assertEqual(calc.add(-1,2), 1)
        self.assertEqual(calc.add(1,-2), -1)
        self.assertEqual(calc.add(-1,-2), -3)

    def test_subtract(self):
        self.assertEqual(calc.subtract(6,2), 4)
        self.assertEqual(calc.subtract(-6,2), -8)
        self.assertEqual(calc.subtract(6,-2), 8)
        self.assertEqual(calc.subtract(-6,-2), -4)

    def test_multiply(self):
        # This test will FAIL because multiply is not correctly written
        # see calc.py for the error
        self.assertEqual(calc.multiply(1,2), 2)
        self.assertEqual(calc.multiply(-1,2), -2)
        self.assertEqual(calc.multiply(1,-2), -2)
        self.assertEqual(calc.multiply(-1,-2), 2)

    def test_divide(self):
        self.assertEqual(calc.divide(4,2), 2)
        self.assertEqual(calc.divide(-4,2), -2)
        self.assertEqual(calc.divide(4,-2), -2)
        self.assertEqual(calc.divide(-4,-2), 2)

# use this so that you do not need command line params
#   to run unit tests
if __name__ == '__main__':
    unittest.main()  
