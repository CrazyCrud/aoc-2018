def count_characters(word):
    return_groups_of_two = 0
    return_groups_of_three = 0

    char_counts = {}
    for char in word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for key, value in char_counts.items():
        if value == 2 and return_groups_of_two == 0:
            return_groups_of_two = 1
        elif value >= 3 and return_groups_of_three == 0:
            return_groups_of_three = 1

    return return_groups_of_two, return_groups_of_three


if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as input:
        groups_of_two_count = 0
        groups_of_three_count = 0
        for line in input:
            line = line.strip()
            groups_of_two, groups_of_three = count_characters(line)
            groups_of_two_count += groups_of_two
            groups_of_three_count += groups_of_three

        checksum = groups_of_two_count * groups_of_three_count

        print("The checksum is {}".format(checksum))
