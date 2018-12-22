import numpy as np


def calc_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y + serial 
    power *= rack_id
    d = str(power)[-3]
    return int(d) - 5


def get_total_power(x, y, serial, size=3):
    power = 0
    for i in range(size):
        for j in range(size):
            power += calc_power(x + i, y + j, serial)
    return power


def part_one():
    """
    Objective:
        Given an 300 x 300 grid, find the subgrid 3x3
        which maximises the power.
        
    Returns the coordinates (x, y) for the top-left corner
    for the subgrid
    """
    # Problem input
    serial = 9424
    
    # Starting values
    max_power = get_total_power(1, 1, serial)
    x, y = 1,1

    # Loop through every possible 3x3 subgrid entirely contained
    # within the 300x300 grid
    for i in range(4, 298):
        for j in range(4, 298):
            power = get_total_power(i, j, serial)
            if power > max_power:
                max_power = power
                x, y = i, j
    
    return x, y


def integral_image(grid):
    # Returns a "summed-area table" of the given input
    # See https://en.wikipedia.org/wiki/Summed-area_table
    result = np.copy(grid)
    # Vertical pass
    for i in range(1, grid.shape[0]):
        result[i, :] += result[i-1, :]

    # Horizontal pass
    for i in range(1, result.shape[1]):
        result[:, i] += result[:, i-1]
    
    return result


def sum_subgrid(grid, x, y, height, width):
    # The sum of a subsquare is computed using its four corner points.
    x = x - 1
    y = y - 1

    a = 0 if x < 0 or y < 0 else grid[x, y]
    b = 0 if x < 0 else grid[x, y+ width]
    c = grid[x+height, y+width]
    d = 0 if y < 0 else grid[x+ height, y]

    return c - b - d + a


def part_two():
    """
    Objective: Over a 300x300 grid, find the subgrid of any square
    size that maximises the sum of subrid values.

    Integral image algorithm, often used in computer vision should
    allow for a summed-area table to be computed once, and then
    finding the sum of any subgrid using only the four corner values.
    
    Ref:
    https://en.wikipedia.org/wiki/Summed-area_table

    """
    # Problem input
    serial = 9424

    # Pre-compute each grid point power
    grid = np.asarray([[calc_power(i, j, serial) for i  in range(1,301)] for j in range(1, 301)])

    # Use the "integral image" algorithm 
    summed_area = integral_image(grid)

    # Starting values
    x, y, size = 0, 0, 1
    max_power = grid[0, 0]

    # For all possible subgrid sizes, loop through possible subgrids entirely 
    # inside the 300x300 grid.
    for s in range(1, 301):
        for i in range(0, 300 - s):
            for j in range(0, 300 - s):
                power = sum_subgrid(summed_area, i, j, s, s)
                if power > max_power:
                    max_power = power
                    x, y, size = i, j, s 

    # Reverse coordinates b.c. problem given uses opposite from numpy.
    return (y + 1, x + 1, size)
