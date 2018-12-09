import re
import numpy as np


def read_input(input_data):
    regex = r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'

    claims = []

    for line in input_data:
        match = re.match(regex, line)

        if match:
            claim = {
                'claim_id': int(match.group(1)),
                'x_offset': int(match.group(2)),
                'y_offset': int(match.group(3)),
                'width': int(match.group(4)),
                'height': int(match.group(5))
            }
            claims.append(claim)

    return claims


def part_1(claims):
    fabric = np.array([[[[]] for j in range(1000)] for i in range(1000)])

    print(fabric.shape)

    for claim in claims:
        x_offset = claim['x_offset']
        y_offset = claim['y_offset']
        id = claim['claim_id']
        width = claim['width']
        height = claim['height']

        # print(id, x_offset, y_offset, width, height)

        for x in range(x_offset, x_offset + width):
            for y in range(y_offset, y_offset + height):
                fabric_field = fabric[x][y]
                fabric_field = np.append(fabric_field, id)
                fabric[x][y] = fabric_field

    number_of_claimed_fields = 0
    for x in range(fabric.shape[0]):
        for y in range(fabric.shape[1]):
            if fabric[x, y].size > 1:
                number_of_claimed_fields += number_of_claimed_fields

    print("{} files are claimed by two or more ids".format(number_of_claimed_fields))


if __name__ == "__main__":
    file = open('input.txt', 'r', encoding='utf-8')

    lines = file.read().split('\n')

    file.close()

    claims = read_input(lines)

    part_1(claims)
