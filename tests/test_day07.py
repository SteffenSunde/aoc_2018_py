import unittest
import aoc_2018_py.day07 as day07

class Test_Day06(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day07.part_one(), "EUGJKYFQSCLTWXNIZMAPVORDBH")

    def test_part_two(self):
        self.assertEqual(day07.part_two(), 1014)

if __name__ == '__main__':
    unittest.main()