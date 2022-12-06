from functools import reduce
import numpy


def day_06(data, debug=False):

    # Get all letters
    small_letters = map(chr, range(ord('a'), ord('z') + 1))

    # Assemble priority dictionary
    priority = dict()
    for prio, letter in enumerate(small_letters, start=1):
        priority[letter] = prio

    beacon_signals = list()
    for line in data:
        beacon_signal = numpy.zeros(len(line), dtype=numpy.int16)
        for pos, item in enumerate(line):
            beacon_signal[pos] = priority[item]
        beacon_signals.append(beacon_signal)

    # Part 1
    print('Part 1')

    beacon_start_pos = list()
    for beacon_signal in beacon_signals:
        # print(f' Next signal {beacon_signal}')
        for pos in range(4, len(beacon_signal)-4):
            marker = numpy.unique(beacon_signal[pos-4:pos])
            if len(marker) == 4:
                beacon_start_pos.append(pos)
                break


    # Part 2
    beacon_start_pos_2 = list()
    for beacon_signal in beacon_signals:
        # print(f' Next signal {beacon_signal}')
        for pos in range(14, len(beacon_signal)-4):
            marker = numpy.unique(beacon_signal[pos-14:pos])
            if len(marker) == 14:
                beacon_start_pos_2.append(pos)
                break

    print(f'\tDay 06')
    print(f'\t\tPart 1: Stream marker pos: {beacon_start_pos}')
    print(f'\t\tPart 2: Stream message marker: {beacon_start_pos_2}\n')

    return beacon_start_pos, beacon_start_pos_2
