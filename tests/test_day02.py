import unittest
import aoc_2018_py.day02 as day02

class Test_Day02(unittest.TestCase):

    def test_part_one(self):
        self.assertEqual(day02.part_one(), 5658)

    def test_part_two(self):
        self.assertEqual(day02.part_two(), "nmgyjkpruszlbaqwficavxneo")

if __name__ == '__main__':
    unittest.main()