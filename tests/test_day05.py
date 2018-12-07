import unittest
import aoc_2018_py.day05 as day05

class Test_Day05(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day05.part_one(), 11042)

    def test_part_two(self):
        self.assertEqual(day05.part_two(), 6872)

if __name__ == '__main__':
    unittest.main()