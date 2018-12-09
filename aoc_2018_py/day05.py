from typing import List

def solve():
    print("Remaining units in polymer chain: {}".format(part_one()))
    print("Reacted polymer, after clean-up: {}".format(part_two()))


def remove_opposite_cases(text: List[str]):
    """
    TODO:
     - Make more efficient (avoid list conversion maybe)
     - Implement Divide and Conquer (recursive)?

    """
    changes = True
    last_passing = False
    while changes and len(text) >= 2:
        changes = False
        i = 1
        while i < len(text):
            if abs(ord(text[i]) - ord(text[i-1])) == 32:
                del(text[i-1:i+1])
                changes = True
                i -= 1
            i += 1
    
    return text


def remove_opposite_cases_dac(text: str):
    if len(text) == 1:
        return text
    elif len(text) == 2:
        if abs(ord(text[0]) - ord(text[1])) == 32:
            return ''
        else:
            return text


def part_one():
    polymer = []
    with open("inputs/day05.input") as data_file:
        polymer.extend(data_file.readline().strip())

    polymer = remove_opposite_cases(polymer)
    return len(polymer)


def part_two():
    """
    Are there any other way than brute force?
    """
    polymer = ""
    with open("inputs/day05.input") as data_file:
        polymer = data_file.readline().strip()

    polymer_lengths = []
    for i in range(26):
        char_upper = chr(65+i)
        char_lower = chr(97+i)
        new_polymer = polymer.replace(char_lower, '')
        new_polymer = new_polymer.replace(char_upper, '')
        polymer_lengths.append(len(remove_opposite_cases(list(new_polymer))))
    
    return min(polymer_lengths)