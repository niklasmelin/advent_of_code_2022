

def day_01(data, debug=False):

    # Part 1
    calories = list()
    elf_calories = 0
    for line in data:
        current_data = line.strip()
        if current_data == '':
            calories.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(current_data)
    calories.append(elf_calories)

    # Get elf with maximum calories
    max_elf_calories = max(calories)

    # Part 2
    calories.sort()
    three_top_elfs = sum(calories[-3:])

    print(f'\tDay 01')
    print(f'\t\tPart 1: Elf with most calories {max_elf_calories}')
    print(f'\t\tPart 2: Top three elfs calories total {three_top_elfs}\n')

    return max_elf_calories, three_top_elfs
