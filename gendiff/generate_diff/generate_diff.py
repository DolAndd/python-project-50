import json


def convert_bool(value):
    if value == True:
        return 'true'
    elif value == False:
        return 'false'
    return value


def gen_diff(pathfile_1, pathfile_2):
    file_1 = json.load(open(pathfile_1, 'r'))
    file_2 = json.load(open(pathfile_2, 'r'))
    result = {}
    result_str = '{\n'
    for i in file_1:
        if i in file_2 and file_1[i] == file_2[i]:
            result[f'  {i}'] = convert_bool(file_1[i])
        elif i in file_2 and file_1[i] != file_2[i]:
            result[f'- {i}'] = convert_bool(file_1[i])
        else:
            result[f'- {i}'] = convert_bool(file_1[i])
    for i in file_2:
        if i in file_1 and file_2[i] != file_1[i]:
            result[f'+ {i}'] = convert_bool(file_2[i])
        elif i not in file_1:
            result[f'+ {i}'] = convert_bool(file_2[i])
    result_dict = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    for key, value in result_dict.items():
        result_str += f' {key}: {value}\n'
    return result_str + '}'
