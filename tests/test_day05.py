import unittest
import aoc_2018_py.day05 as day05

class Test_Day04(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day05.part_one(), 11042)

    def test_part_two(self):
        self.assertTrue(False) 

if __name__ == '__main__':
    unittest.main()