

def solve():
    print("Total overlapping fabric: {}".format(part_one()))
    print("Id of claim with no overlap: {}".format(part_two()))


def tokenize(claim: str):
    (i, _, pos, size) = tuple(claim.split(' '))
    claim_id = i[1:]
    pos_x, pos_y = pos.split(',')
    width, height = size.split('x')
    pos_y = pos_y[:-1]

    return (int(claim_id), int(pos_x), int(pos_y), int(width), int(height))


def part_one():
    with open("inputs/day03.input") as data_file:
        fabric = {}
        for line in data_file:
            (_, pos_x, pos_y, width, height) = tokenize(line)
            for i in range(pos_x, pos_x + width):
                for j in range(pos_y, pos_y + height):
                    if (i, j) in fabric:
                        fabric[(i, j)] += 1
                    else:
                        fabric[(i, j)] = 1
        overlapping = len([1 for _, val in fabric.items() if val > 1])
        return overlapping


def part_two():
    claims = []
    with open("inputs/day03.input") as data_file:
        for line in data_file:
            claims.append(tokenize(line))
    
    fabric = {}
    for (claim_id, start_x, start_y, width, height) in claims:
        for i in range(start_x, start_x + width + 1):
            for j in range(start_y, start_y + height + 1):
                if (i, j) in fabric:
                    fabric[(i, j)] += 1
                else:
                    fabric[(i, j)] = 1

    for (claim_id, start_x, start_y, width, height) in claims:
        not_overlapping = True
        for i in range(start_x, start_x + width + 1):
            for j in range(start_y, start_y + height + 1):
                if fabric[(i, j)] > 1:
                    not_overlapping = False
        if not_overlapping:
            return claim_id

    return None