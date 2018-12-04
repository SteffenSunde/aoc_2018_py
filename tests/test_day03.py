import unittest
import aoc_2018_py.day03 as day03

class Test_Day02(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day03.part_one(), 120408)

    def test_part_two(self):
        self.assertEqual(day03.part_two(), 1276)

if __name__ == '__main__':
    unittest.main()