import math
import unittest

# Function that takes in radius and returns circ of circle
def calculate_circumference(r): # This is the unit
    return r * 2 * math.pi

# create a test class which inherits from TestCase
class code_test(unittest.TestCase):
    # define a method
    def test_circumference(self): # This is the test case
        # If the methods 1st and 2nd parameter values are equal the assertion will pass
        self.assertEqual(calculate_circumference(5),31.41592653589793) # i.e. if function returns 31.4592...
    # Test edge case of circle with radius of 0
    def test_circumference_zero(self):
        actual = calculate_circumference(0)
        self.assertEqual(actual,0)

    # Test if function correctly raises error if non-number passed in as argument
    def test_false_circumference(self):
        self.assertRaises(calculate_circumference("Five"))

# Call function to run the testcases
unittest.main() # This is the test runner

