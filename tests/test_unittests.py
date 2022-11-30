import pathlib
import unittest


# Get location of this file for relative relation of custom lib
__this_file__ = pathlib.Path(__file__)
__this_path__ = __this_file__.parent.resolve()

input_data_path = __this_path__.parent.joinpath('inputs/')

# Get path to input file
test_data_path = __this_path__.joinpath('test_data')


def load_data(file_path):
    data = list()
    with open(file_path) as file_handle:
        for line in file_handle.readlines():
            data.append(line.strip())
    return data


class AdventOfCodeTests(unittest.TestCase):

    def test_1_09_test_data(self):
        """
        Day 1 - Test Data
        """
        day_no = '01'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (15, 1134)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_01 import day_01
            result = day_01(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_2_09_actual_data(self):
        """
        Day 1 - Actual Data
        """
        day_no = '01'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (524, 1235430)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_01 import day_01
            result = day_01(data)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

