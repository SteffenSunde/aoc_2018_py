from typing import List, Tuple

def solve():
    print("Sum of all metadata entries: {}".format(part_one()))
    print("Value of root node: {}".format(part_two()))


class Node(object):
    # A simple recursive data structure to represent a tree with data and children nodes.
    def __init__(self):
        self.data = []  # type: List[int]
        self.children = []  # type: List[Node]
        self.end = None  # type: int

    def add_child(self, node):
        self.children.append(node)


def read_ints(file_path: str) -> List[int]:
    with open(file_path) as datafile:
        integers = [int(x) for x in datafile.read().split()]
    return integers


def parse_tree(input_data: List[int]) -> Node:
    # Parses the list of integers as a recursive tree, returning its root node

    pointer = 0  # Offset to continuously run through input list
    while pointer < len(input_data):
        num_children, num_data = input_data[:2]
        pointer += 2
        node = Node()

        # Read children nodes first
        for i in range(num_children):
            child = parse_tree(input_data[pointer:])
            pointer += child.end
            node.add_child(child)

        # Data comes after the children nodes
        for j in range(num_data):
            node.data.append(input_data[pointer])
            pointer += 1
        
        break  # Parse only one node at the time.
    node.end = pointer # Add the end pointer so that the next node knows where to start.
    return node


def sum_metadata(node: Node) -> int:
    # Recursively traverses the tree to sum all metadata
    acc = 0
    acc += sum(node.data)
    acc += sum([sum_metadata(c) for c in node.children])
    return acc


def evaluate(node: Node) -> int:
    # Computes the value of a node
    if len(node.children) == 0:
        return sum(node.data)
    else:
        num_children = len(node.children)
        return sum([evaluate(node.children[i-1]) for i in node.data if i <= num_children and i > 0])


def part_one():
    integers = read_ints("inputs/day08.input")
    int_tree = parse_tree(integers)
    return sum_metadata(int_tree)


def part_two():
    integers = read_ints("inputs/day08.input")
    int_tree = parse_tree(integers)
    return evaluate(int_tree) 
