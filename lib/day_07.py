import pathlib


def traverse_folders(file, line_no=0):
    folders, files = [0, 0]

    if line.startswith('$ cd'):
        current_folder = line.split()[-1]
        folder_depth.append(current_folder)
        if current_folder not in folders:
            folders[current_folder] = list()

    return folders, files


def day_07(data, debug=False):

    folders = dict()
    folders_path = dict()

    line_no = 0
    folder_depth = list()
    current_folder = None
    current_path = pathlib.Path('/')

    while True:
        line = data[line_no]

        if line.startswith('$ cd'):
            current_folder = line.split()[-1]
            current_path = current_path / current_folder

            if current_path.as_posix() not in folders_path:
                folders_path[current_path.as_posix()] = list()

        if line.startswith('$') and 'ls' in line.split():
            while True:
                if line_no >= len(data):
                    break
                line = data[line_no]
                if line.startswith('$ cd ..'):
                    try:
                        current_path = current_path.parents[0]
                        print(f"\tChange UP from {current_path.as_posix()} to {current_path.parents[0].as_posix()}")
                    except:
                        pass

                elif line.startswith('$ cd'):
                    current_folder = line.split()[-1]
                    current_path = current_path / current_folder
                    print(f"\tChange DOWN from {current_path.parents[0].as_posix()} to {current_path.as_posix()}")

                if line.startswith('dir'):
                   pass
                elif not line.startswith('$'):
                    size, name = line.split()
                    if not current_path.as_posix() in folders_path:
                        folders_path[current_path.as_posix()] = list()
                    folders_path[current_path.as_posix()].append(int(size))

                if line_no >= len(data):
                    break

                line_no += 1
        line_no += 1

        if line_no >= len(data):
            break

    # Part 1
    print(' Part 1')
    for path, file_sizes in folders_path.items():
        size = 0
        for file_size in file_sizes:
            size += int(file_size)
        print(f'\t{path} - {size}')

    # Part 2
    print(' Part 2')

    print(f'\tDay 07')
    print(f'\t\tPart 1: Stream marker pos: {0}')
    print(f'\t\tPart 2: Stream message marker: {0}\n')

    return 0, 0
