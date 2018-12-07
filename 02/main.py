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


def part_1(input_data):
    groups_of_two_count = 0
    groups_of_three_count = 0
    for line in input_data:
        line = line.strip()
        groups_of_two, groups_of_three = count_characters(line)

        groups_of_two_count += groups_of_two
        groups_of_three_count += groups_of_three

    checksum = groups_of_two_count * groups_of_three_count

    print("The checksum is {}".format(checksum))


def are_words_common(word_1, word_2):
    assert len(word_1) == len(word_2)

    equality = []
    for i in range(len(word_1)):
        equality.append(word_1[i] == word_2[i])

    return equality


def get_resulting_word(word, equality):
    return "".join([word[i] for i in range(len(word)) if equality[i]])


def part_2(input_data):
    for i in range(len(input_data)):
        for j in range(i, len(input_data)):
            word_1, word_2 = input_data[i], input_data[j]
            if word_1 == word_2:
                continue
            equality = are_words_common(word_1, word_2)
            if len([common_character for common_character in equality if not common_character]) == 1:
                print("Words with one different character are {} and {}".format(word_1, word_2))
                print("Without the differing character it is {}".format(get_resulting_word(word_1, equality)))


if __name__ == "__main__":
    input_file = open('input.txt', 'r', encoding='utf-8')
    lines = input_file.read().split("\n")
    input_file.close()

    part_1(lines)

    part_2(lines)
