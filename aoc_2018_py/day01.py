

def solve():
    print("Total change in frequency: {}".format(part_one()))
    print("First reoccurring frequency: {}".format(part_two()))


def part_one():
    with open("inputs/day01.input") as data_file:
        total_change = 0
        for line in data_file:
            total_change += int(line)

    return total_change


def part_two():
    with open("inputs/day01.input") as data_file:
        found = {}
        first_repeat = None
        total_change = 0
        while first_repeat is None:
            for line in data_file:
                total_change += int(line)
                if first_repeat is None:
                    if total_change in found:
                        first_repeat = total_change
                    else:
                        found[total_change] = True
            data_file.seek(0)

        return first_repeat