import unittest
import aoc_2018_py.day10 as day10

class Test_Day10(unittest.TestCase):

    def test_part_two(self):
        self.assertEqual(day10.part_one(), 10710)

if __name__ == '__main__':
    unittest.main()