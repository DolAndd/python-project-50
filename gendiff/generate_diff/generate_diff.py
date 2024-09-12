import json

with open('gendiff/parsed_files/file1.json', 'r') as json_file:
    data_1 = json.load(json_file)

with open('gendiff/parsed_files/file2.json', 'r') as json_file:
    data_2 = json.load(json_file)

def gen_diff(file_1, file_2):
    result = {}
    for i in file_1:
        if i in file_2 and str(file_1[i]) == str(file_2[i]):
            result[i] = str(file_1[i])
        elif i in file_2 and str(file_1[i]) != str(file_2[i]):
            result[f'- {i}'] = str(file_1[i])
        else:
            result[f'- {i}'] = str(file_1[i])
    for i in file_2:
        if i in file_1 and str(file_1[i]) != str(file_2[i]):
            result[f'+ {i}'] = str(file_2[i])
        elif i not in file_1:
            result[f'+ {i}'] = str(file_2[i])
    return result

print(gen_diff(data_1, data_2))