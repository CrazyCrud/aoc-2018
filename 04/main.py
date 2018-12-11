import re
import read_input


def sort_input(input_data):
    reg_ex = r'([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})'

    input_data_sorted = []

    records = []

    for line in input_data:

        match = re.match(reg_ex, line)

        if match:
            record = {
                'year': int(match.group(1)),
                'month': int(match.group(2)),
                'day': int(match.group(3)),
                'hours': int(match.group(4)),
                'minutes': int(match.group(5))
            }

            print(record)

            records.append(record)

    return input_data_sorted


def part_1(input_data):
    input_data_sorted = sort_input(input_data)


if __name__ == "__main__":
    input_data = read_input.read_all_lines_of_file('04')

    part_1(input_data)
