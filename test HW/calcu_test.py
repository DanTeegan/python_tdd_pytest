# Here we are importing the class Calcu from the calcu file
from calcu import Calcu

# Here we are importing pytest
import pytest

# Here we are importing unittest
import unittest

# Here we create a class called Calcu_test. We have placed unittest.TestCase in order to run a test
class Calcu_Test(unittest.TestCase):

    # Here we are defining our object of Calcu which referances the object made in the calcu file
    simple_calcu = Calcu()

    # Here we have a test to check the sq root using the method from the Calcu class
    def test_sqrt(self):
        self.assertEqual(self.simple_calcu.find_sqrt(16), 4)

    # Here we have a test to check the round up function ceil. Again a method from the Calcu class
    def test_ceil(self):
        self.assertEqual(self.simple_calcu.find_ceil(9.8), 10)

    # Here we have a test to check the round down function floor. Again a method from the Calcu class
    def test_floor(self):
        self.assertEqual(self.simple_calcu.find_floor(1032.32), 1032)