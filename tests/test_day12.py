import unittest
import numpy as np
import numpy.testing as npt
import aoc_2018_py.day12 as day12


class Test_Day12(unittest.TestCase):


    def test_part_one(self):
        self.assertEqual(day12.part_one(), 2995)
    
    
    def test_part_two(self):
        self.assertEqual(day12.part_two(), 3650000000377)


if __name__ == '__main__':
    unittest.main()