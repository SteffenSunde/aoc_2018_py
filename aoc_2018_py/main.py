import day01
import day02
import day04
import day05
import time

if __name__ == '__main__':
    t0 = time.time()
    # print("Day 1 solutions: ")
    # day01.solve()

    # print("\nDay 2 solutions: ")
    # day02.solve()

    # print("\nDay 4 solutions: ")
    # day04.solve()

    print("\nDay 5 solutions: ")
    day05.solve()

    t1 = time.time()

    print("Total time spent: {}".format(t1-t0))