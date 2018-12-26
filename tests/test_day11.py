import unittest
import numpy as np
import numpy.testing as npt
import aoc_2018_py.day11 as day11

class Test_Day11(unittest.TestCase):

    def test_calc_power(self):
        self.assertEqual(day11.calc_power(3, 5, 8), 4)
        self.assertEqual(day11.calc_power(122, 79, 57), -5)
        self.assertEqual(day11.calc_power(217, 196, 39), 0)
        self.assertEqual(day11.calc_power(101, 153, 71), 4)


    def test_integral_image(self):
        magic_square = np.asarray([[31, 2, 4, 33, 5, 36], 
                                   [12, 26, 9, 10, 29, 25],
                                   [13, 17, 21, 22, 20, 18], 
                                   [24, 23, 15, 16, 14, 19],
                                   [30, 8, 28, 27, 11, 7], 
                                   [1, 35, 34, 3, 32, 6]])
        summed_area = np.asarray([[ 31,  33,  37,  70,  75, 111],
                                [ 43,  71,  84, 127, 161, 222],
                                [ 56, 101, 135, 200, 254, 333],
                                [ 80, 148, 197, 278, 346, 444],
                                [110, 186, 263, 371, 450, 555],
                                [111, 222, 333, 444, 555, 666]])
        npt.assert_allclose(day11.integral_image(magic_square), summed_area)


    def test_sum_subgrid(self):
        magic_square = np.asarray([[31, 2, 4, 33, 5, 36], 
                                   [12, 26, 9, 10, 29, 25],
                                   [13, 17, 21, 22, 20, 18], 
                                   [24, 23, 15, 16, 14, 19],
                                   [30, 8, 28, 27, 11, 7], 
                                   [1, 35, 34, 3, 32, 6]])

        summed_area = day11.integral_image(magic_square)

        self.assertEqual(day11.sum_subgrid(summed_area, 2, 1, 3, 3), np.sum(magic_square[2:5, 1:4]))
        self.assertEqual(day11.sum_subgrid(summed_area, 0, 1, 2, 3), np.sum(magic_square[0:2, 1:4]))
        self.assertEqual(day11.sum_subgrid(summed_area, 0, 3, 4, 3), np.sum(magic_square[0:4, 3:6]))
        self.assertEqual(day11.sum_subgrid(summed_area, 0, 0, 2, 2), np.sum(magic_square[0:2, 0:6]))



    def test_part_one(self):
        self.assertEqual(day11.part_one(), (243, 72))
    
    
    def test_part_two(self):
        self.assertEqual(day11.part_two(), (229, 192, 11))

if __name__ == '__main__':
    unittest.main()