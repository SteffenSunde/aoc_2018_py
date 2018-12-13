import unittest
import aoc_2018_py.day08 as day08

class Test_Day08(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day08.part_one(), 44338)

    def test_part_two(self):
        self.assertEqual(day08.part_two(), 37560)

if __name__ == '__main__':
    unittest.main()