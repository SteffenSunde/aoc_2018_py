import unittest
import aoc_2018_py.day06 as day06

class Test_Day06(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day06.part_one(), 4771)

    def test_part_two(self):
        self.assertEqual(day06.part_two(), 39149)

if __name__ == '__main__':
    unittest.main()