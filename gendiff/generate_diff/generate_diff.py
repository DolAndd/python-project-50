from gendiff.generate_diff.parser import files_parser


def convert_bool(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value


def convert_dict_to_str(dictionary):
    result_str = ''
    for key, value in dictionary.items():
        result_str += f' {key}: {value}\n'
    return result_str


def gen_diff(pathfile_1, pathfile_2):
    file_1 = files_parser(pathfile_1)
    file_2 = files_parser(pathfile_2)
    result = {}
    for i in file_1:
        if i in file_2 and file_1[i] == file_2[i]:
            result[f'  {i}'] = convert_bool(file_1[i])
        else:
            result[f'- {i}'] = convert_bool(file_1[i])
    for i in file_2:
        if (i in file_1 and file_2[i] != file_1[i]) or (i not in file_1):
            result[f'+ {i}'] = convert_bool(file_2[i])
    result_dict = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    return '{\n' + convert_dict_to_str(result_dict) + '}'
