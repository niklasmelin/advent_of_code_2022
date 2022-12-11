from functools import reduce
import numpy


def day_08(data, debug=False):

    rows = len(data)
    cols = len(data[0])

    trees = numpy.zeros((rows, cols), dtype=numpy.int16)
    visible_trees = numpy.zeros((rows, cols), dtype=numpy.bool)

    # Get Header end
    for row, line in enumerate(data):
        for col, tree in enumerate(line):
            trees[row, col] = int(tree)



    # Part 1
    print('Part 1')

    # Part 2
    print('Part 2')

    print(f'\tDay 04')
    print(f'\t\tPart 1: Top crates: {0}')
    print(f'\t\tPart 2: Top crates: {0}\n')

    return 1, 1
