def has_frequency_been_reached_twice(results, result):
    count = results.count(result)
    return count == 2


if __name__ == "__main__":
    frequency_result = 0

    input = open('input.txt', 'r', encoding='utf-8')
    input.seek(0)

    frequency_results = []

    frequency = input.readline()
    frequency_result += int(frequency)

    frequency_results.append(frequency_result)

    while has_frequency_been_reached_twice(frequency_results, frequency_result) is False:
        frequency = input.readline()

        if frequency == '':
            input.seek(0)
            frequency = input.readline()

        frequency_result += int(frequency)
        frequency_results.append(frequency_result)

    output_string = "The resulting frequency is {}".format(frequency_result)
    print(output_string)

    input.close()
