import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer("hello")
        with self.assertRaises(TypeError):
            max_integer(123)
