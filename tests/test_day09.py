import unittest
import aoc_2018_py.day09 as day09

class Test_Day09(unittest.TestCase):

    def test_max_scores(self):
        self.assertEqual(day09.max_score(9, 25), 32)
        self.assertEqual(day09.max_score(10, 1618), 8317)
        self.assertEqual(day09.max_score(13, 7999), 146373)
        self.assertEqual(day09.max_score(17, 1104), 2764)
        self.assertEqual(day09.max_score(21, 6111), 54718)
        self.assertEqual(day09.max_score(30, 5807), 37305)

    def test_part_one(self):
        self.assertEqual(day09.part_one(), 388131)

    def test_part_two(self):
        self.assertEqual(day09.part_two(), 3239376988)

if __name__ == '__main__':
    unittest.main()