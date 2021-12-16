import unittest
import ReviewThree

class Test3(unittest.TestCase):
    def test_removeInRange(self):
        start = [0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16]
        end = [2, 4, 6, 8, 10, 12, 14, 16]
        ReviewThree.removeInRange(start, 1, 50, 0)
        self.assertEqual(start, end)

    def test_removeInRange2(self):
        start = [2, 4, 6, 8, 10, 12, 14, 0, 16]
        end = [2, 4, 6, 8, 10, 12, 14, 16]
        ReviewThree.removeInRange2(start, 1, 50, 0)
        self.assertEqual(start, end)