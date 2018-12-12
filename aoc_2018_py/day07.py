
def solve():
    print("The correct order of instructions: {}".format(part_one()))
    print("Total time spent on all instructions: {}".format(part_two()))


def part_one():
    # Read set of instructions from file
    requires_table = {}
    with open("inputs/day07.input") as data_file:
        for line in data_file:
            char = line[36]
            req = line[5]
            if char in requires_table:
                requires_table[char][req] = True
            else:
                requires_table[char] = {req: True}
            if not req in requires_table:
                requires_table[req] = {}

    # Loop through instructions to find the correct order
    order = []
    while len(requires_table) != 0:
        letters = [char for char, require in requires_table.items() if len(require) == 0]
        letter = sorted(letters)[0] 
        for _, requires in requires_table.items():
            if letter in requires:
                del(requires[letter])
        del(requires_table[letter])
        order.append(letter)

    return "".join(order)


def part_two():
    # Read set of instructions from file
    requires_table = {}
    with open("inputs/day07.input") as data_file:
        for line in data_file:
            char = line[36]
            req = line[5]
            if char in requires_table:
                requires_table[char][req] = True
            else:
                requires_table[char] = {req: True}
            if not req in requires_table:
                requires_table[req] = {}

    # Now work on an instruction (letter) takes time "60 + ord(letter) - 64"
    available_workers = 5
    working_queue = {}
    order = []
    time = 0
    while len(requires_table) != 0:
        # Finding the instructions that can be started
        letters = sorted([char for char, require in requires_table.items() if len(require) == 0])
        for letter in letters:
            del(requires_table[letter])

        # Put available workers to work!
        for i in range(available_workers):
            if i < len(letters):
                working_queue[letters[i]] = ord(letters[i]) - 4
                available_workers -= 1

        # Update work counter for all instructions currently worked on
        for letter, workload in working_queue.items():
            working_queue[letter] = workload - 1

        # Check for finished instructions
        finished_instructions = []
        for letter, workload in working_queue.items():
            if workload == 0:
                # Removing the instruction as requirement for the other instructions
                for _, requires in requires_table.items():
                    if letter in requires:
                        del(requires[letter])
                available_workers += 1
                finished_instructions.append(letter)
        
        for instruction in finished_instructions:
            del(working_queue[instruction])

        # Increment timer
        time += 1

    # Finally, get the remaining time on the last set of instructions
    time += sum([val for _, val in working_queue.items()]) # This has probably a bug if multiple jobs remains

    return time