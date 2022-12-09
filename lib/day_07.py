import pathlib

path_sizes = dict()

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

        if line.startswith('$ cd ..'):
            try:
                current_path = current_path.parents[0]
                print(f"\t Change UP from {current_path.as_posix()} to {current_path.parents[0].as_posix()}")
            except:
                pass

        elif line.startswith('$ cd'):
            current_folder = line.split()[-1]
            current_path = current_path / current_folder

            if current_path.as_posix() not in folders_path:
                folders_path[current_path.as_posix()] = list()
            try:
                print(f"\t Change DOWN from {current_path.parents[0].as_posix()} to {current_path.as_posix()}")
            except:
                print('\t Change to root')

        if line.startswith('dir'):
           pass
        elif not line.startswith('$'):
            try:
                size, name = line.split()
            except:
                print(line)
                raise
            if not current_path.as_posix() in folders_path:
                folders_path[current_path.as_posix()] = list()
            folders_path[current_path.as_posix()].append(int(size))

        if line_no >= len(data):
            break

        line_no += 1

        if line_no >= len(data):
            break

    # Part 1
    print(' Part 1')
    print('   Total file size per path:')
    path_file_size = dict()
    for path, file_sizes in folders_path.items():
        size = 0
        for file_size in file_sizes:
            size += int(file_size)
        print(f'\t{path} - {size}')
        path_file_size[path] = size

    # Relationships
    relatives = dict()
    for path in folders_path.keys():
        children = [i for i in folders_path.keys() if i.startswith(path) and i is not path]
        if debug:
            print(f' Path: {path} has children {children}')
        relatives[path] = children

    def sum_children(start_child, _relatives, _path_file_size):
        global path_sizes
        total_children = 0
        for child in _relatives[start_child]:
            total_children += sum_children(child, _relatives, _path_file_size)
        # Sum children sizes and sizes in this path
        total = total_children + path_file_size[start_child]
        path_sizes[start_child] = total
        return total

    total = sum_children('/', relatives, path_file_size)


    print('Sizes recursively for each path')
    for path, size in path_sizes.items():
        print(f' Path: {path} - Size {size}')

    limit = 100000
    total_under_limit = 0
    print('Sizes recursively for each path')
    for path, size in path_sizes.items():
        if size < limit:
            total_under_limit += size


    # Part 2
    print(' Part 2')

    print(f'\tDay 07')
    print(f'\t\tPart 1: Stream marker pos: {total_under_limit}')
    print(f'\t\tPart 2: Stream message marker: {0}\n')

    return total_under_limit, 0
