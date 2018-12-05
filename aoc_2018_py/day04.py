#import operator
from typing import List, Tuple

def solve():
    print("Guard id multiplied by start time: {}".format(part_one()))
    print("Part two not implemented yet!")


def most_overlapping(nap_list: List[Tuple[int, int]]):
    """
    Should return the single integer being overlapped the most
    Input list contains tuples representing a range(start, end) 
    not including end.
    of the list [(x1, x2), (y1, y2) ..]  all the 
    """
    overlapping = {}
    for nap in nap_list:
        for minute in range(nap[0], nap[1]):
            if minute in overlapping:
                overlapping[minute] += 1
            else:
                overlapping[minute] = 1

    return max(overlapping, key=lambda x: overlapping[x])


def part_one():
    log = []
    with open("inputs/day04.input") as data_file:
        for line in data_file:
            log.append(line)

    # Sort works well when date string is in ISO format
    log.sort(key=lambda x: x[1:17])

    # Now running through and adding up all sleeping time..
    sleep_table = {}
    guard_id = None
    for entry in log:
        time = int(entry[15:17])
        if entry.split(' ')[2] == "Guard": 
            guard_id = int(entry.split(' ')[3][1:])
        elif entry.split(' ')[2] == "falls":
            start_sleep = time
        elif entry.split(' ')[2] == "wakes":
            end_sleep = time # Current min is regarded as awake
            if guard_id in sleep_table:
                sleep_table[guard_id].append((start_sleep, end_sleep))
            else:
                sleep_table[guard_id] = [(start_sleep, end_sleep)]
    
    k = list(sleep_table.keys())
    v = list(sleep_table.values())
    most_sleepy_guard = k[v.index(max(v, 
            key=lambda sleep_list: sum(x[1] - x[0] for x in sleep_list)))]
    
    # Need to rather find the minute he is most likely to sleep!
    best_time = most_overlapping(sleep_table[most_sleepy_guard])
    
    return most_sleepy_guard * best_time