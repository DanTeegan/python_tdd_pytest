from calcu import Calcu
import pytest
import unittest

class Calcu_Test(unittest.TestCase):

    simple_calcu = Calcu()

    def test_sqrt(self):
        self.assertEqual(self.simple_calcu.find_sqrt(16), 4)

    def test_ceil(self):
        self.assertEqual(self.simple_calcu.find_ceil(9.8), 10)