

def solve():
    print("The checksum of lists of boxes: {}".format(part_one()))
    print("The correct box id: {}".format(part_two()))


def count_twos_and_threes(s: str):
    characters = {}
    for char in s:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    two = len([k for k, v in characters.items() if v == 2]) > 0 
    three = len([k for k, v in characters.items() if v == 3]) > 0
    return (two, three)


def part_one():
    twos = 0
    threes = 0
    with open("inputs/day02.input") as data_file:
        for line in data_file:
            two, three = count_twos_and_threes(line)
            if two: twos += 1
            if three: threes += 1
    return twos * threes


def compare_ids(id1: str, id2: str):
    if len(id1) != len(id2): return False
    diff = len(id1)
    common = ""
    for i,c in enumerate(id1):
        if id1[i] == id2[i]:
            common += id1[i]
            diff -= 1
        
    return diff, common


def part_two():
    with open("inputs/day02.input") as data_file1:
        for id1 in data_file1:
            with open("inputs/day02.input") as data_file2:
                for id2 in data_file2:
                    diff, common = compare_ids(id1, id2)
                    if diff == 1:
                        return common.rstrip()