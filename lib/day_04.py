from functools import reduce
import numpy


def day_04(data, debug=False):

    # Example data: 2-4,6-8

    # Part 1
    print('Part 1')
    complete_overlaps = 0

    for line in data:
        # Get data and convert to integers
        x12, y12 = line.split(',')
        x1, x2 = x12.split('-')
        y1, y2 = y12.split('-')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 <= y1 and y2 <= x2:
            if debug:
                print(f'\tOverlapping 1: {line}', f'[{x1}, {x2}], [{y1}, {y2}]')
            complete_overlaps += 1
        elif y1 <= x1 and x2 <= y2:
            if debug:
                print(f'\tOverlapping 2: {line}', f'{y1} <= {x1}, {y1 <= x1}, {x2} <= {y2} {x2 <= y2}')
            complete_overlaps += 1
        else:
            if debug:
                print(f'\t{line}  [{x1}, {x2}], [{y1}, {y2}]')

    # Part 2
    print('\n\n Part 2')
    partly_overlaps = 0

    for line in data:
        # Get data and convert to integers
        x12, y12 = line.split(',')
        x1, x2 = x12.split('-')
        y1, y2 = y12.split('-')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        section_1 = range(x1, x2 + 1)
        section_2 = range(y1, y2 + 1)

        if y1 in section_1 or y2 in section_1:
            if debug:
                print(f'\tPartly overlapping 1: {line}', f'[{x1}, {x2}], [{y1}, {y2}]')
            partly_overlaps += 1
        elif x1 in section_2 or x2 in section_2:
            if debug:
                print(f'\tPartly overlapping 2: {line}', f'[{x1}, {x2}], [{y1}, {y2}]')
            partly_overlaps += 1
        else:
            if debug:
                print(f'\t{line}  [{x1}, {x2}], [{y1}, {y2}]')

    print(f'\tDay 04')
    print(f'\t\tPart 1: Completely overlapping sections: {complete_overlaps}')
    print(f'\t\tPart 2: Partly overlapping sections: {partly_overlaps}\n')

    return complete_overlaps, partly_overlaps
