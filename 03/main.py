import re


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
    fabric = [[[] for j in range(1000)] for i in range(1000)]

    for claim in claims:
        x_offset = claim['x_offset']
        y_offset = claim['y_offset']
        id = claim['claim_id']
        width = claim['width']
        height = claim['height']

        for x in range(x_offset, x_offset + width):
            for y in range(y_offset, y_offset + height):
                fabric_field = fabric[x][y]
                fabric_field.append(id)
                fabric[x][y] = fabric_field

    number_of_claimed_fields = 0
    for x in range(0, len(fabric)):
        for y in range(0, len(fabric[0])):
            if len(fabric[x][y]) > 1:
                number_of_claimed_fields += 1

    print("{} files are claimed by two or more ids".format(number_of_claimed_fields))

    return fabric


def part_2(fabric):
    unique_ids = set()

    x_length = len(fabric)
    y_length = len(fabric[0])

    for x in range(0, x_length):
        for y in range(0, y_length):
            fabric_field = fabric[x][y]

            if len(fabric_field) == 1:
                unique_ids.add(fabric_field[0])

    for x in range(0, x_length):
        for y in range(0, y_length):
            fabric_field = fabric[x][y]

            if len(fabric_field) > 1:
                for claim_id in fabric_field:
                    unique_ids.discard(claim_id)

    print("Unique ids are {}".format(unique_ids))
    print(len(unique_ids))


if __name__ == "__main__":
    file = open('input.txt', 'r', encoding='utf-8')

    lines = file.read().split('\n')

    file.close()

    claims = read_input(lines)

    fabric = part_1(claims)

    part_2(fabric)
