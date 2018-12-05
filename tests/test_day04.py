import unittest
import aoc_2018_py.day04 as day04

class Test_Day04(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day04.part_one(), 76357)

    def test_part_two(self):
        self.assertEqual(day04.part_two(), 41668)
        pass

if __name__ == '__main__':
    unittest.main()