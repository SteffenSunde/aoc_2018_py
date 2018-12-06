from typing import List

def solve():
    print("Remaining units in polymer chain: {}".format(part_one()))
    print("Not implemented yet!")

def remove_opposite_cases(text: List[str]):
    changes = True
    last_passing = False
    while changes or last_passing:
        changes = False
        i = 1
        while i < len(text):
            if abs(ord(text[i]) - ord(text[i-1])) == 32:
                del(text[i-1:i+1])
                changes = True
                i -= 1
            i += 1
        
        if not changes and not last_passing:
            last_passing = True
        elif not changes and last_passing:
            last_passing = False
            
        if len(text) < 2:
            break
    
    return text
    

def part_one():
    polymer = []
    with open("inputs/day05.input") as data_file:
        polymer.extend(data_file.readline().strip())

    polymer = remove_opposite_cases(polymer)
    return len(polymer)


def part_two():
    """
    Same as part one, only now we first need to find the one character in the polymer
    which is hindering the collapse of the polymer the most.

    - Identify problematic char
    - Remove char
    - Find length of collapsed polymer

    """
    pass