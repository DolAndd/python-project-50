from gendiff.generate_diff.parser import files_parser
from gendiff.generate_diff.stylish import stylish


def convert_bool(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def gen_diff(file_1, file_2):
    added = set(file_2) - set(file_1)
    removed = set(file_1) - set(file_2)
    unchanged = set(file_1) & set(file_2)
    diff = {}
    for i in added:
        diff.update({i: {'type': 'added', 'value': convert_bool(file_2[i])}})
    for i in removed:
        diff.update({i: {'type': 'removed', 'value': convert_bool(file_1[i])}})
    for i in unchanged:
        if file_1[i] == file_2[i]:
            diff.update({i: {'type': 'unchanged',
                             'value': convert_bool(file_1[i])}})
        else:
            if isinstance(file_1[i], dict) and isinstance(file_2[i], dict):
                diff.update({i: {'type': 'nested',
                                 'value': gen_diff(file_1[i], file_2[i])}})
            else:
                diff.update({i: {'type': 'changed',
                                 'old_value': convert_bool(file_1[i]),
                                 'new_value': convert_bool(file_2[i])}})
    return dict(sorted(diff.items()))


def generate_diff(pathfile_1, pathfile_2):
    file_one = files_parser(pathfile_1)
    file_two = files_parser(pathfile_2)
    tree = gen_diff(file_one, file_two)
    return stylish(tree)
