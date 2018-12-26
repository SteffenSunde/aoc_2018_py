from typing import Tuple, List
import numpy as np

def solve():
    print("Sum of plants after 20 generations: {}".format(part_one()))
    print("Sum of plants after 50 billion generations: {}".format(part_two()))

def boolean_plant(c: str) -> int:
    if c == "#":
        return 1
    else: 
        return 0
   

def read_plant_data(file_path: str) -> Tuple:
    # Reads the input data into binary data ('#' -> 1, '.' -> 0).
    initial_state = None
    rules = {}
    with open(file_path) as data_file:
        first_line = data_file.readline()[15:-1]
        initial_state = np.asarray([1 if c == '#' else 0 for c in first_line])
        data_file.readline()
        for line in data_file.readlines():
            pattern = tuple([boolean_plant(c) for c in line[:5]])
            rules[pattern] = boolean_plant(line[-2])

    return initial_state, rules


def part_one():
    """
    Given a list of data points either 0 or 1, and a list of rules for 
    each data point to evolve from generation to the next, find the state
    after 20 generations.

    Return the sum of positions in list, where the data point have vaue 1.

    """
    pots, rules = read_plant_data("inputs/day12.input")
    pots_last = np.copy(pots)
    for _ in range(20):
        pots_last = np.hstack(([0]*5, pots_last, [0]*5))
        pots = np.hstack(([0]*5, pots, [0]*5))
        for i in range(2, len(pots) - 3):
            pattern = tuple(pots_last[i-2:i+3])
            if pattern in rules:
                pots[i] = rules[pattern]
        pots_last = pots

    result = sum([position - 100 for position, plant in enumerate(pots) if plant])
    return result


def part_two():
    """
    Same as part one, only now for 50 billion generations.
    This time, lets not add unnecessary zeros, and rather 
    trim the list and keep track of the offset as we go.

    After inspections, the plants seem to stabilize into
    a linear growth. Therefore one can find the generation
    for which this linear growth takes place, then extrapolate.

    y = a x + b

    where
     - a is the linear coefficient
     - x is the generation number
     - b is the value after transient

    """
    import matplotlib.pyplot as plt

    pots, rules = read_plant_data("inputs/day12.input")
    pots_last = pots  # Pots from the last generation
    offset = 0  # The number of pots added at the beginning
    generations = []  # For inspecting growth 
    a = None  
    for gen in range(500):
        pots = np.hstack(([0]*5, pots, [0]*5))
        pots_last = np.copy(pots)
        offset += 5
        for i in range(2, len(pots) - 3):
            pattern = tuple(pots_last[i-2:i+3])
            if pattern in rules:
                pots[i] = rules[pattern]
        #changes.append(changes = np.sum(np.logical_xor(pots, pots_last)))  # For debugging
        pots = np.trim_zeros(pots, "f")
        offset -= len(pots_last) - len(pots)
        pots = np.trim_zeros(pots, "b")
        result = sum([position - offset for position, plant in enumerate(pots) if plant])
        generations.append(result)

        # Simply assuming constant growth based on four points (may fail)
        if len(generations) > 4 and generations[-1] - generations[-2] == generations[-2] - generations[-3]:
            a = generations[-1] - generations[-2]
            break

    # plt.plot(generations)  # For inspecting data
    # plt.show()
    return a * (50_000_000_000-gen-1) + result
