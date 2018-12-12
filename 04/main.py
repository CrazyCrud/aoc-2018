import re
import read_input


def get_minutes_of_each_guard(input_data):
    regex_begin = r'\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] Guard #([0-9]+) begins shift'
    regex_sleep = r'\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] falls asleep'
    regex_awake = r'\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] wakes up'

    return_minutes_of_each_guard = {}
    return_minutes_data = [[] for x in range(60)]

    guard_current = None

    minute_start_of_sleep = None
    minute_end_of_sleep = None

    for line in input_data:
        print(line)
        match = re.match(regex_begin, line)

        if match:
            guard_current = (int)(match.group(6))
            continue

        match = re.match(regex_sleep, line)
        if match:
            minute_start_of_sleep = (int)(match.group(5))
            continue

        match = re.match(regex_awake, line)
        if match:
            minute_end_of_sleep = (int)(match.group(5))
            sleep_duration = minute_end_of_sleep - minute_start_of_sleep

            if guard_current in return_minutes_of_each_guard:
                return_minutes_of_each_guard[guard_current].append(sleep_duration)
            else:
                return_minutes_of_each_guard[guard_current] = [sleep_duration]

            for i in range(minute_start_of_sleep, minute_end_of_sleep):
                return_minutes_data[i].append(guard_current)

    return return_minutes_of_each_guard, return_minutes_data


def part_1(input_data):
    input_data = sorted(input_data)
    minutes_of_each_guard, minutes_data = get_minutes_of_each_guard(input_data)

    current_sleep_duration_max = 0
    guard = None
    for key, sleep_durations in minutes_of_each_guard.items():
        sleep_duration_max = max(sleep_durations)

        if sleep_duration_max > current_sleep_duration_max:
            current_sleep_duration_max = sleep_duration_max
            guard = key

    current_most_frequent_minute = 0
    minute = None
    for index, minute_data in enumerate(minutes_data):
        frequent_minute = minute_data.count(guard)
        if frequent_minute > current_most_frequent_minute:
            current_most_frequent_minute = frequent_minute
            minute = index

    print("Guard {} sleeps most frequent on minute {} and the solution is {}".format(guard, minute, guard * minute))


if __name__ == "__main__":
    input_data = read_input.read_all_lines_of_file('04')

    part_1(input_data)
