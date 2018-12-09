
def solve():
    print("Largest safe area that isn't infinite: {}".format(part_one()))
    print("Area containing points within total distance of 10 000: {}".format(part_two()))

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def part_one():
    points = []
    x_min, x_max, y_min, y_max = 0,0,0,0

    with open("inputs/day06.txt") as data_file:
        for line in data_file:
            point_x = int(line.split(', ')[0])
            point_y = int(line.split(', ')[1])
            points.append((point_x, point_y))
            x_min = min(x_min, point_x)
            x_max = max(x_max, point_x)
            y_min = min(y_min, point_y)
            y_max = max(y_max, point_y)


    areas = [0 for _ in points]  # Initialize all areas to be zero
    edges = []  # Note edge areas to be removed due to being infinite
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            min_distances = 100000000000000000000000  # Maybe a better way to do this.
            several = False
            point_id = 0
            for i, point in enumerate(points):
                distance = manhattan_distance(point, (x, y))
                if distance < min_distances:
                    min_distances = distance
                    several = False
                    point_id = i
                elif distance == min_distances:
                    several = True
            if x == x_min or x == x_max-1 or y == y_min or y == y_max-1:
                edges.append(point_id)
            if not several:
                areas[point_id] += 1
    for p in edges:
        areas[p] = 0
    
    return max(areas)


def part_two():
    coordinates = []
    x_min, x_max, y_min, y_max = 0,0,0,0
    with open("inputs/day06.txt") as data_file:
        for line in data_file:
            point_x = int(line.split(', ')[0])
            point_y = int(line.split(', ')[1])
            coordinates.append((point_x, point_y))
            x_min = min(x_min, point_x)
            x_max = max(x_max, point_x)
            y_min = min(y_min, point_y)
            y_max = max(y_max, point_y)

    # Find size of region containing all locations which have a total
    # distance to all coordinates less than 10 000.

    # Area is contained within the limits set by the outermost points..
    area = 0
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            total_distance = 0
            for point in coordinates:
                total_distance += manhattan_distance(point, (x, y))
            if total_distance < 10000:
                area += 1

    return area