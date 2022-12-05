from functools import reduce
import numpy


class Cargo:

    def __init__(self, initial_container_placement):

        # Each pile of container has a number in the dict
        self.containers = dict()
        # A list of all moves
        self.moves = list()
        # Number of container stacks
        self.number_of_stacks = 0

        self.__place_containers__(initial_container_placement)

    def __place_containers__(self, initial_container_placement):

        # Populate container rows
        container_rows = initial_container_placement[-1].strip()
        for pile, j in enumerate(range(0, len(container_rows), 4)):
            container = container_rows[j:j + 4].strip()
            self.containers[int(container.strip())] = list()

        self.number_of_stacks = int(j)

        placement = initial_container_placement[0:-1]
        placement.reverse()

        for container_names in placement:
            i = len(container_names)
            for pile, j in enumerate(range(0, i, 4), start=1):
                pile = int(pile)
                container = container_names[j:j+4].strip()
                if not container == '':
                    self.containers[pile].append(container)

    def move(self, amount, from_pile, to_pile):
        # Sanity check
        if from_pile in self.containers and to_pile in self.containers and amount <= len(self.containers[from_pile]):
            for i in range(amount):
                container = self.containers[from_pile][-1]
                self.containers[from_pile].pop(-1)
                self.containers[to_pile].append(container)
        else:
            print(f'\t Invalid move: Move {amount} from {from_pile} to {to_pile}')

    def move_9001(self, amount, from_pile, to_pile):
        # Sanity check
        if from_pile in self.containers and to_pile in self.containers and amount <= len(self.containers[from_pile]):
            containers = self.containers[from_pile][-amount:]
            del self.containers[from_pile][-amount:]
            self.containers[to_pile].extend(containers)
        else:
            print(f'\t Invalid move: Move {amount} from {from_pile} to {to_pile}')


def day_05(data, debug=False):

    # Get Header end
    for line_no, line in enumerate(data):
        if line.strip() == '':
            break
    header_end = line_no

    # Part 1
    print('Part 1')
    docker_container = Cargo(data[0:header_end])
    print('Cargo initial')
    for key, item in docker_container.containers.items():
        print(key, item)

    for line in data[header_end + 1:]:
        temp = line.split(' ')
        amount, from_pile, to_pile = int(temp[1]), int(temp[3]), int(temp[5])
        docker_container.move(amount, from_pile, to_pile)

    print('Cargo after move')
    for key, item in docker_container.containers.items():
        print(key, item)

    top_crates = list()
    for key, item in docker_container.containers.items():
        top_crates.append(docker_container.containers[key][-1][1])

    # Part 2
    print('\n\n Part 2')
    docker_container = Cargo(data[0:header_end])
    print('Cargo initial')
    for key, item in docker_container.containers.items():
        print(key, item)

    for line in data[header_end + 1:]:
        temp = line.split(' ')
        amount, from_pile, to_pile = int(temp[1]), int(temp[3]), int(temp[5])
        docker_container.move_9001(amount, from_pile, to_pile)

    print('Cargo after move_9001')
    for key, item in docker_container.containers.items():
        print(key, item)

    top_crates_2 = list()
    for key, item in docker_container.containers.items():
        top_crates_2.append(docker_container.containers[key][-1][1])


    print(f'\tDay 04')
    print(f'\t\tPart 1: Top crates: {"".join(top_crates)}')
    print(f'\t\tPart 2: Top crates: {"".join(top_crates_2)}\n')

    return top_crates, top_crates_2
