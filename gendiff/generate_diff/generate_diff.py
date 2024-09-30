from gendiff.generate_diff.parser import get_file_data
from gendiff.formaters.format import choose_formater
from gendiff.generate_diff.diff_list import gen_diff


def generate_diff(pathfile_1, pathfile_2, format_name='stylish'):
    file_one = get_file_data(pathfile_1)
    file_two = get_file_data(pathfile_2)
    tree = gen_diff(file_one, file_two)
    return choose_formater(tree, format_name)
