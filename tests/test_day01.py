import unittest
import aoc_2018_py.day01 as day01

class Test_Day01(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day01.part_one(), 505)

    def test_part_two(self):
        self.assertEqual(day01.part_two(), 72330)

if __name__ == '__main__':
    unittest.main()