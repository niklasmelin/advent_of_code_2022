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


def load_raw_data(file_path):
    data = list()
    with open(file_path) as file_handle:
        for line in file_handle.readlines():
            data.append(line)
    return data

class AdventOfCodeTests(unittest.TestCase):

    def test_01_1_test_data(self):
        """
        Day 1 - Test Data
        """
        day_no = '01'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (24000, 45000)

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

    def test_01_2_actual_data(self):
        """
        Day 1 - Actual Data
        """
        day_no = '01'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (70720, 207148)

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

    def test_02_1_test_data(self):
        """
        Day 2 - Test Data
        """
        day_no = '02'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (15, 12)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_02 import day_02
            result = day_02(data, debug=False)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_02_2_actual_data(self):
        """
        Day 2 - Actual Data
        """
        day_no = '02'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (9759, 12429)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_02 import day_02
            result = day_02(data)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_03_1_test_data(self):
        """
        Day 3 - Test Data
        """
        day_no = '03'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (157, 70)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_03 import day_03
            result = day_03(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_03_2_actual_data(self):
        """
        Day 3 - Actual Data
        """
        day_no = '03'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (7908, 2838)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_03 import day_03
            result = day_03(data)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_04_1_test_data(self):
        """
        Day 4 - Test Data
        """
        day_no = '04'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (2, 4)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_04 import day_04
            result = day_04(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_04_2_actual_data(self):
        """
        Day 4 - Actual Data
        """
        day_no = '04'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (441, 861)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_04 import day_04
            result = day_04(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_05_1_test_data(self):
        """
        Day 5 - Test Data
        """
        day_no = '05'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (['C', 'M', 'Z'],
                               ['M', 'C', 'D'])

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_raw_data(input_path)

            # Crunch data
            from lib.day_05 import day_05
            result = day_05(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_05_2_actual_data(self):
        """
        Day 5 - Actual Data
        """
        day_no = '05'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (['D', 'H', 'B', 'J', 'Q', 'J', 'C', 'C', 'W'],
                               ['W', 'J', 'V', 'R', 'L', 'S', 'J', 'J', 'T'])

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_raw_data(input_path)

            # Crunch data
            from lib.day_05 import day_05
            result = day_05(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_06_1_test_data(self):
        """
        Day 6 - Test Data
        """
        day_no = '06'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = ([7, 5, 6, 10, 11], [19, 23, 23, 26])

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_06 import day_06
            result = day_06(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_06_2_actual_data(self):
        """
        Day 6 - Actual Data
        """
        day_no = '06'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = ([1343], [2193])

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_06 import day_06
            result = day_06(data, debug=False)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_07_1_test_data(self):
        """
        Day 6 - Test Data
        """
        day_no = '07'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (95437, 24933642)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_07 import day_07
            result = day_07(data, debug=True)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_07_2_actual_data(self):
        """
        Day 7 - Actual Data
        """
        day_no = '07'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (1449447, 8679207)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_07 import day_07
            result = day_07(data, debug=False)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_11_1_test_data(self):
        """
        Day 6 - Test Data
        """
        day_no = '11'
        try:
            print(f'\n Day {day_no} - Test', flush=True)

            expected_result = (10605, 2713310158)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}_test.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_11 import day_11
            result = day_11(data, debug=False)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise

    def test_11_2_actual_data(self):
        """
        Day 11 - Actual Data
        """
        day_no = '11'
        try:
            print(f'\n Day {day_no} - Actual', flush=True)

            expected_result = (1449447, 8679207)

            # Source data
            input_path = input_data_path.joinpath(f'{day_no}.txt')

            # Load data
            data = load_data(input_path)

            # Crunch data
            from lib.day_11 import day_11
            result = day_11(data, debug=False)

            self.assertEqual(expected_result, result, msg=f'Day {day_no} - Test problem does not work for example data')
        except (AssertionError, FileNotFoundError):
            print(f" *** Day {day_no} FAILED: Problem does not work for example data", flush=True)
            raise
