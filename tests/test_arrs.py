import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 10, 100, 48, 542], 5, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([21, 22, 23, 24]), [21, 22, 23, 24])
        self.assertEqual(arrs.my_slice([21, 22, 23, 24], end=2), [21, 22])
        self.assertEqual(arrs.my_slice([], 1, 5), [])
        self.assertEqual(arrs.my_slice([]), [])
        with self.assertRaises(TypeError):
            arrs.my_slice(25698, 1, 5)
