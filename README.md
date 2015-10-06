# azatfmkhf
__author__ = 'student'

import unittest

import lib

class LibTest(unittest.TestCase):

    def test_even(self):
        self.assertEqual(lib.even(2),True)
        self.assertEqual(lib.even(8),True)
        self.assertEqual(lib.even(1),False)
        self.assertEqual(lib.even(-1),False)
        self.assertEqual(lib.even(-3),False)
        
  unittest.main(verbosity=2)
