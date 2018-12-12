from typing import List, Tuple

def solve():
    print("Sum of all metadata entries: {}".format(part_one()))
    print("Value of root node: {}".format(part_two()))


class Node(object):
    def __init__(self):
        self.data = []
        self.children = []
        self.end = None

    def add_child(self, node):
        self.children.append(node)


def read_ints(file_path: str):
    with open(file_path) as datafile:
        integers = [int(x) for x in datafile.read().split()]
    return integers


def parse_tree(input_data: List[int]) -> Node:

    pointer = 0  # Offset to continuously run through input list
    while pointer < len(input_data):
        num_children, num_data = input_data[:2]  # This will fail if data is not proper
        pointer += 2
        node = Node()

        # Read children first
        for i in range(num_children):
            child = parse_tree(input_data[pointer:])
            pointer += child.end
            node.add_child(child)

        # Data comes after the children nodes
        for j in range(num_data):
            node.data.append(input_data[pointer])
            pointer += 1
        
        break  # Parse only one node at the time.
    node.end = pointer
    return node


def sum_metadata(node: Node):
    acc = 0
    acc += sum(node.data)
    acc += sum([sum_metadata(c) for c in node.children])
    return acc


def evaluate(node: Node) -> int:
    # Calculate the value of a node
    # If a node has no child nodes, its valuue is the sum of its metadata
    # If a node has children, its nodes are counted by the indicies given by metadata
    #   - If index found in metadata does not exist, ignore
    #   - A child node can be counted multiple times
    #   - A metadata entry of 0 does not refer to any child nodes.
    # :::: Find the value of the root node
    if len(node.children) == 0:
        return sum(node.data)
    else:
        num_children = len(node.children)
        value_of_children = sum([evaluate(node.children[i-1]) for i in node.data if i <= num_children and i > 0])
        return sum(node.data) + value_of_children

integers = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
tree = parse_tree(integers)
print(evaluate(tree))

def part_one():
    integers = read_ints("inputs/day08.input")
    int_tree = parse_tree(integers)
    return sum_metadata(int_tree)


def part_two():
    integers = read_ints("inputs/day08.input")
    int_tree = parse_tree(integers)
    return evaluate(int_tree)  # 2601 is too low # 42811 is too high





print("day08 imported")