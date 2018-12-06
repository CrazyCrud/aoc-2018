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

    char_counts['word'] = word

    return return_groups_of_two, return_groups_of_three, char_counts


def are_words_common(word_1, word_2):
    assert len(word_1['word']) == len(word_2['word'])

    word_1_chars = list(word_1.keys())
    word_2_chars = list(word_2.keys())
    common_keys = set(word_1_chars) - (set(word_1_chars) - set(word_2_chars))

    if len(common_keys) == (len(word_1_chars) - 1):
        return True
    else:
        return False


if __name__ == "__main__":
    words_chars = []

    with open('input.txt', 'r', encoding='utf-8') as input:
        groups_of_two_count = 0
        groups_of_three_count = 0
        for line in input:
            line = line.strip()
            groups_of_two, groups_of_three, char_counts = count_characters(line)

            groups_of_two_count += groups_of_two
            groups_of_three_count += groups_of_three

            words_chars.append(char_counts)

        checksum = groups_of_two_count * groups_of_three_count

        print("The checksum is {}".format(checksum))

    for index_1, word_char_1 in enumerate(words_chars):
        for index_2, word_char_2 in enumerate(words_chars):
            if index_1 == index_2:
                continue
            if are_words_common(word_char_1, word_char_2):
                pass
