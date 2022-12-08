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

            folder_depth.append(current_folder)
            if current_folder not in folders:
                folders[current_folder] = list()

            if current_path.as_posix() not in folders_path:
                folders_path[current_path.as_posix()] = list()

        if line.startswith('$') and 'ls' in line.split():
            while True:
                if line_no >= len(data):
                    break
                print(line_no, len(data))
                line = data[line_no]

                if line.startswith('$ cd ..'):
                    print(folder_depth)
                    if len(folder_depth) > 1:
                        print(f" Change up from {current_folder} to {folder_depth[-2]}")
                        line_no -= 1
                        folder_depth.pop(-1)
                        current_folder = folder_depth[-1]
                    else:
                        print('At root already!')

                    try:
                        current_path = current_path.parents[1]
                    except:
                        pass

                elif line.startswith('$ cd'):
                    print(f" Change down from {folder_depth[-1]} to  {line.split()[-1]}")
                    current_folder = line.split()[-1]
                    folder_depth.append(current_folder)

                    current_path = current_path / current_folder

                if line.startswith('dir'):
                    folder_name = line.split()[-1]
                    folders[folder_name] = list()

                    folders_path[current_path.as_posix()] = list()

                elif not line.startswith('$'):
                    size, name = line.split()
                    folders[current_folder].append(size)

                    folders_path[current_path.as_posix()].append(size)

                    folders_path[current_path.as_posix()].append(int(size))


                if line_no >= len(data):
                    break

                line_no += 1
                print(line_no)
        line_no += 1

        if line_no >= len(data):
            break
    print(folders)



    # Part 1
    print('Part 1')

    for folder, file_sizes in folders.items():
        size = 0
        for file_size in file_sizes:
            size += int(file_size)
        print(f'\t{folder} - Size: {file_size}')

    for path, file_sizes in folders_path.items():
        print(f'{path} - {file_sizes}')

    # Part 2

    print(f'\tDay 07')
    print(f'\t\tPart 1: Stream marker pos: {0}')
    print(f'\t\tPart 2: Stream message marker: {0}\n')

    return 0, 0
