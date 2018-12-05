from typing import List, Tuple

def solve():
    print("Guard id multiplied by start time: {}".format(part_one()))
    print("Guard id multiplied by most occuring minute of sleep: {}".format(part_two()))


def part_one():
    """
    Strategy one for finding the correct minute to sneak in
    """
    sleep_table = generate_sleeping_table("inputs/day04.input")
    
    k = list(sleep_table.keys())
    v = list(sleep_table.values())

    # Find the id of the most sleepy guard
    most_sleepy_guard = k[v.index(max(v,
        key=lambda sleep_list: sum(x[1] - x[0] for x in sleep_list)))]
    
    # Need to rather find the minute he is most likely to sleep!
    best_time, _ = most_overlapping(sleep_table[most_sleepy_guard])
    
    return most_sleepy_guard * best_time


def part_two():
    sleep_table = generate_sleeping_table("inputs/day04.input")
    
    # Now find the guard most likely to sleep on the same minute
    guard_id = None
    max_occurring = -1
    preferred_minute = None
    for guard in sleep_table:
        minute, number = most_overlapping(sleep_table[guard])
        if number > max_occurring:
            max_occurring = number
            guard_id = guard
            preferred_minute = minute

    return guard_id * preferred_minute


def generate_sleeping_table(log_file):
    log = []
    with open(log_file) as data_file:
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
            end_sleep = time
            if guard_id in sleep_table:
                sleep_table[guard_id].append((start_sleep, end_sleep))
            else:
                sleep_table[guard_id] = [(start_sleep, end_sleep)]

    return sleep_table


def most_overlapping(nap_list: List[Tuple[int, int]]):
    """
    Takes a list of tuples, each containing start and stop for a range.
    Should return the single tuple (x, y) 
    
    where
        x: Most occuring minute
        y: Number of occurrences
    """
    overlapping = {}
    for nap in nap_list:
        for minute in range(nap[0], nap[1]):
            if minute in overlapping:
                overlapping[minute] += 1
            else:
                overlapping[minute] = 1

    most_occurring_minute = max(overlapping, key=lambda x: overlapping[x])
    number_of_occurrences = overlapping[most_occurring_minute]

    return most_occurring_minute, number_of_occurrences
