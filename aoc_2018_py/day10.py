import numpy as np
import re
from typing import List, Tuple
import math
import matplotlib.pyplot as plt  # For debugging


class Point:
    def __init__(self, pos_x, pos_y, vel_x=0, vel_y=0):
         self.position = (pos_x, pos_y)
         self.velocity = (vel_x, vel_y)

    def inc(self, t=1):
        return Point(self.position[0] + self.velocity[0]*t, 
                     self.position[1] + self.velocity[1]*t,
                     self.velocity[0], self.velocity[1])
    
    def __repr__(self):
        return "Pos: {}, vel: {}".format(self.position, self.velocity)


def read_points(file_path) -> List[Point]:
    points = []
    with open(file_path) as data_file:
        for line in data_file:
            numbers = list(map(int, re.findall("(\-?\d+)", line)))
            points.append(Point(*numbers))
    return points


def parse_sky(stars: List[Point]) -> str:
    # Takes a list of points and returns a printable string 
    # representation.
    min_x, min_y, max_x, max_y = bounding_box_corners(stars)

    grid = [[' ']*(max_x - min_x + 1) for _ in range(min_y, max_y + 1)]
    for p in stars:
        grid[p.position[1] - min_y][p.position[0] - min_x] = '#'

    message = ""
    for row in grid:
        message += "".join(row) + '\n'
    return message


def bounding_box(stars: List[Point]) -> int:
    # Computes the half circumference of the bounding box.
    x_min = stars[0].position[0]
    x_max = stars[0].position[0]
    y_min = stars[0].position[1]
    y_max = stars[0].position[1]

    for i in range(1, len(stars)):
        x_min = min(x_min, stars[i].position[0])
        x_max = max(x_max, stars[i].position[0])
        y_min = min(y_min, stars[i].position[1])
        y_max = max(y_max, stars[i].position[1])

    return (x_max - x_min) + (y_max - y_min)


def bounding_box_corners(stars: List[Point]) -> Tuple[int, int, int, int]:
    # Computes the half circumference of the bounding box.
    x_min = stars[0].position[0]
    x_max = stars[0].position[0]
    y_min = stars[0].position[1]
    y_max = stars[0].position[1]

    for i in range(1, len(stars)):
        x_min = min(x_min, stars[i].position[0])
        x_max = max(x_max, stars[i].position[0])
        y_min = min(y_min, stars[i].position[1])
        y_max = max(y_max, stars[i].position[1])

    return x_min, y_min, x_max, y_max


def part_one():
    """
    Reads point poisitons and velocities from file and integrates
    the velocity until a message appears.
    
    Assumptions:
     - All points contributes to the message
     - Points velocities are constant
        - Minimising the bounding box will reveal the message
        - Golden section search should do the trick
    """
    points = read_points("inputs/day10.input")

    # Golden section search, assuming minima will be within [0, 20000]
    low = 0
    high = 20000
    # graph = [high, low]  # For debugging (Convergence plot)
    while(high - low > 1): 
        box_low = bounding_box([p.inc(low) for p in points])
        box_high = bounding_box([p.inc(high) for p in points])
        if box_high > box_low:
            high = low + 0.6108*(high - low)
        elif box_high < box_low:
            low = high - 0.6108*(high - low)
    #     graph.append(high)
    #     graph.append(low)
    # plt.plot(graph)
    # plt.show()
    
    sec = int((high + low) / 2)
    message = [p.inc(sec) for p in points]
    
    print(parse_sky(message))

    return sec

part_one()