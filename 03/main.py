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
    pass


if __name__ == "__main__":
    file = open('input.txt', 'r', encoding='utf-8')

    lines = file.read().split('\n')

    claims = read_input(lines)

    part_1(claims)