

def day_01(data, debug=False):

    depths = list()
    for line in data:
        depths.append(int(line.strip()))

    # Part 1
    increasing = 0
    for no in range(1, len(depths)):
        if depths[no] > depths[no-1]:
            increasing += 1

    # Part 2
    sweeping = 0
    for no in range(0, len(depths)-3):
        a = depths[no:no + 3]
        b = depths[no + 1:no + 3 + 1]
        if sum(a) < sum(b):
            status = 'increasing'
        elif sum(a) == sum(b):
            status = 'no change'
        elif sum(a) > sum(b):
            status = 'decreasing'
        else:
            status = ' ERROR'

        if debug:
            print(f' Window 1 {sum(a):>4}', a, f', Window 2 {sum(b):>4}', b, f', {status}')
        if sum(a) < sum(b):
            sweeping += 1

    print(f'\tDay 01')
    print(f'\t\tPart 1: There are {increasing} depths increasing')
    print(f'\t\tPart 2: There are sweeping {sweeping} depths increasing\n')

    return increasing, sweeping
