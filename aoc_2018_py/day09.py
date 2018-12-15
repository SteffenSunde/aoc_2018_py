from typing import Tuple, List

def solve():
    print("Winning score in game: {}".format(part_one()))
    print("New winning score: {}".format(part_two()))


def get_game_data(file_path: str) -> Tuple[int, int]:
    import re
    with open(file_path) as data_file:
        num_players, num_marbles = re.findall("(\d+)", data_file.readline())
        return (int(num_players), int(num_marbles))


def max_score_list(num_players: int, num_marbles: int) -> int:
    # Slower than using doubly linked lists ofc.
    # This one fails on rare occations...
    # E.g. for (13, 7999) it returns 146071...
    current = 1
    circle = [0] 
    scores = [0 for _ in range(num_players)]
    jumps = 0
    for i in range(1, num_marbles+1):
        if i % 23 == 0:
            current -= 7
            scores[i % num_players] += i + circle[current]
            circle = circle[:current] + circle[current+1:]
            jumps += 1
        else:
            # Rotating the list pointer("current")
            if i < 3 or current == len(circle) -1:
                current = 1
            else:
                current += 2  # Some corner cases are missing here...
            circle = circle[:current] + [i] + circle[current:]
    return(max(scores))


def part_one() -> int:
    num_players, num_marbles = get_game_data("inputs/day09.input")
    maximum_score = max_score(num_players, num_marbles)
    return maximum_score


def max_score(num_players: int, num_marbles: int) -> int:
    from collections import deque
    scores = [0 for _ in range(num_players)]
    circle = deque()
    circle.append(0)
    for i in range(1, num_marbles+1):
        if i % 23 == 0:
            circle.rotate(7)
            scores[i % num_players] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
    return(max(scores))


def part_two() -> int:
    # What would the new winning Elf's score be if the 
    # number of the last marble were 100 times larger?
    # There might be a O(1) answer to this?
    # Lets brute force this anyways.
    num_players, num_marbles = get_game_data("inputs/day09.input")
    num_marbles *= 100
    return max_score(num_players, num_marbles)