from functools import reduce
import numpy


def day_03(data, debug=False):

    # Get all letters
    small_letters = map(chr, range(ord('a'), ord('z') + 1))
    big_letters = map(chr, range(ord('A'), ord('Z') + 1))

    # Assemble priority dictionary
    priority = dict()
    for prio, letter in enumerate(small_letters, start=1):
        priority[letter] = prio
    for prio, letter in enumerate(big_letters, start=27):
        priority[letter] = prio

    # Part 1
    sum_duplicate_prio = 0
    for line in data:
        no_items = len(line)
        per_compartment = int(no_items/2)

        np_array = numpy.zeros(no_items, dtype=numpy.int32)
        for pos, letter in enumerate(line):
            np_array[pos] = priority[letter]

        # Find indices of duplicates in compartments
        dupe_prio = numpy.intersect1d(np_array[0:per_compartment],
                                      np_array[per_compartment:])
        # Add prio to sum
        sum_duplicate_prio += dupe_prio[0]

    # Part 2
    badge_group_prio_sum = 0
    for i in range(0, len(data), 3):
        packs = dict()
        for j in range(0, 3):
            no_items = len(data[i+j])
            packs[j] = numpy.zeros(no_items, dtype=numpy.int32)
            for pos, letter in enumerate(data[i+j]):
                packs[j][pos] = priority[letter]

        # Get the unique prio
        bage_group_prio = reduce(numpy.intersect1d, (packs[0], packs[1], packs[2]))

        # Sum up the prios
        badge_group_prio_sum += bage_group_prio[0]

    print(f'\tDay 03')
    print(f'\t\tPart 1: Sum of the priorities {sum_duplicate_prio}')
    print(f'\t\tPart 2: Top three elfs calories total {badge_group_prio_sum}\n')

    return sum_duplicate_prio, badge_group_prio_sum
