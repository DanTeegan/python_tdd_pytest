import pytest
import unittest
from conv import *

class Conv_test(unittest.TestCase):

    simple_conv = Conv()

    def convert(self):
        self.assertEqual(self.simple_conv.convert(10, 2.54), 25.4)
