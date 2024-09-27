from gendiff.formaters.stylish import get_stylish_format
from gendiff.formaters.plain import get_plain_format
from gendiff.formaters.json import get_json_format


def choose_formater(diff, format_name):
    if format_name == 'stylish':
        return get_stylish_format(diff)
    elif format_name == 'plain':
        return get_plain_format(diff)
    elif format_name == 'json':
        return get_json_format(diff)
