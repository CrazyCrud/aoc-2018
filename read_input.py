import os


def read_all_lines_of_file(day, file_name='input'):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '{}'.format(day), '{}.txt'.format(file_name))

    file = open(file_path, 'r', encoding='utf-8')

    lines = file.read().split('\n')

    file.close()

    return lines
