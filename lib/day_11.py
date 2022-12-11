from functools import reduce
import numpy
from math import floor


class Monkey:

    def __init__(self, input_data, debug=False):
        self.debug = debug
        self.monkey_no = None
        self.items = list()
        self.divisible_by = 0
        self.divisible_true = -1
        self.divisible_false = -1
        self.operation = list()
        self.inspected_items = 0

        # Monkey number
        self.monkey_no = int(input_data[0][-2])

        # Starting items
        for i in input_data[1].split(':')[-1].split(','):
            self.items.append(int(i))

        # Operation
        self.operation = input_data[2].split('=')[-1].strip().split(' ')[1:]

        # Test condition
        self.divisible_by = int(input_data[3].split()[-1])

        # Monkey to pass along to
        self.divisible_true = int(input_data[4].split()[-1])
        self.divisible_false = int(input_data[5].split()[-1])

        if self.debug:
            print(f' Monkey {self.monkey_no}\n',
                  f'\t Starting items: {self.items}')
            if {self.operation[1]} == 'old':
                print(f'\t Use {self.operation[0]} and "old')
            else:
                print(f'\t Use {self.operation[0]} and {self.operation[1]}')
            print(f'\t Test divisable by: {self.divisible_by}\n',
                  f'\t\t True:  Throw to monkey: {self.divisible_true}\n',
                  f'\t\t False: Throw to monkey: {self.divisible_false}',
                  )

    def inspection(self, managed_risk=True):

        inspection_list = list()
        for item_no, item in enumerate(self.items):

            # Update number of inspections
            self.inspected_items += 1

            if self.operation[1] == 'old':
                if self.debug:
                    print(f'\t Use {self.operation[0]} and "old')
                new_worry_level = eval(f'{item} {self.operation[0]} {item}')
            else:
                if self.debug:
                    print(f'\t Use {self.operation[0]} and {self.operation[1]}')
                new_worry_level = eval(f'{item} {self.operation[0]} {self.operation[1]}')

            if managed_risk:
                # Divide worry level by 3
                new_worry_level = floor(new_worry_level / 3)

            if new_worry_level % self.divisible_by == 0:
                # Dividable without a rest
                inspection_list.append([new_worry_level, self.divisible_true])
                if self.debug:
                    print('\t Dividable')
            else:
                # Not dividable without a rest
                inspection_list.append([new_worry_level, self.divisible_false])
                if self.debug:
                    print('\t Not Dividable')

            if self.debug:
                print(f' Levels: {self.items[item_no] } -> {new_worry_level}')

        # All items have been inspected and monkey has passed them along
        self.items = list()

        if self.debug:
            print(f'\t Monkey {self.monkey_no} - Item list: {inspection_list}')

        return inspection_list

    def add_item(self, item):
        if self.debug:
            print(f' Monkey {self.monkey_no} received item {item}')
        self.items.append(item)


def day_11(data, debug=False):

    # Part 1
    print('Part 1')
    rounds_to_play = 20

    # Populate monkeys
    monkeys = dict()
    monkey_no = 0
    for i in range(0, len(data), 7):
        print()
        monkeys[monkey_no] = Monkey(data[i:i+6], debug=debug)
        monkey_no += 1

    for i in range(1, rounds_to_play + 1):
        for a_monkey, monkey in monkeys.items():
            inspected_items = monkey.inspection()

            for item, monkey_no in inspected_items:
                monkeys[monkey_no].add_item(item)

        if debug:
            print(f'\t Played rounds: {i}')
        for a_monkey, monkey in monkeys.items():
            if debug:
                print(f' Monkey: {monkey.monkey_no}: {monkey.items}')

    # Get Monkey business
    passes = list()
    for a_monkey, monkey in monkeys.items():
        passes.append(monkey.inspected_items)
    print(passes)
    passes.sort()
    monkey_business = passes[-2] * passes[-1]

    # Part 2
    print('Part 2')

    rounds_to_play = 10000

    # Populate monkeys
    monkeys = dict()
    monkey_no = 0
    for i in range(0, len(data), 7):
        print()
        monkeys[monkey_no] = Monkey(data[i:i + 6], debug=debug)
        monkey_no += 1

    for i in range(1, rounds_to_play + 1):
        for a_monkey, monkey in monkeys.items():
            inspected_items = monkey.inspection(managed_risk=False)

            for item, monkey_no in inspected_items:
                monkeys[monkey_no].add_item(item)

        if debug:
            print(f'\t Played rounds: {i}')
        for a_monkey, monkey in monkeys.items():
            if debug:
                print(f' Monkey: {monkey.monkey_no}: {monkey.items}')

    # Get Monkey business
    passes = list()
    for a_monkey, monkey in monkeys.items():
        passes.append(monkey.inspected_items)
    print(passes)
    passes.sort()
    monkey_business2 = passes[-2] * passes[-1]

    print(f'\tDay 04')
    print(f'\t\tPart 1: Monkey business: {monkey_business}')
    print(f'\t\tPart 2: Top crates: {monkey_business2}\n')

    return monkey_business, monkey_business2
