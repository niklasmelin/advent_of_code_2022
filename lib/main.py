import pathlib
from datetime import datetime


def load_data(file_path):
    data = list()
    with open(file_path) as file_handle:
        for line in file_handle.readlines():
            data.append(line.strip())
    return data


def _day_01():
    from lib.day_01 import day_01

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/01.txt')
    # Load the data from file
    input_data = load_data(input_data_path)

    day_01(input_data)


def _day_02():
    from lib.day_02 import day_02

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/02.txt')
    # Load the data from file
    input_data = load_data(input_data_path)

    day_02(input_data)


def _day_03():
    from lib.day_03 import day_03

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/03.txt')
    # Load the data from file
    input_data = load_data(input_data_path)

    day_03(input_data)


def _day_04():
    from lib.day_04 import day_04

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/04_test.txt')
    # input_data_path = pathlib.Path().joinpath('inputs/04.txt')

    # Load the data from file
    input_data = load_data(input_data_path)

    day_04(input_data)


def _day_05():
    from lib.day_05 import day_05

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/05_test.txt')

    # Load the data from file
    input_data = load_data(input_data_path)

    day_05(input_data)


def _day_06():
    from lib.day_06 import day_06

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/06_test.txt')

    # Load the data from file
    input_data = load_data(input_data_path)

    day_06(input_data)


def _day_07():
    from lib.day_07 import day_07

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/07.txt')

    # Load the data from file
    input_data = load_data(input_data_path)

    day_07(input_data)


def _day_08():
    from lib.day_08 import day_08

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/08_test.txt')

    # Load the data from file
    input_data = load_data(input_data_path)

    day_08(input_data)


def _day_09():
    from lib.day_09 import day_09

    # Path to input data
    input_data_path = pathlib.Path().joinpath('inputs/09_test.txt')

    # Load the data from file
    input_data = load_data(input_data_path)

    day_09(input_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    _day_01()
