def gen_diff(file_1, file_2):
    union_key = sorted(file_2 | file_1)
    diff_tree = []
    for key in union_key:
        if key not in file_1:
            diff_tree.append({'type': 'added', 'key': key,
                              'value': file_2[key]})
        elif key not in file_2:
            diff_tree.append({'type': 'removed', 'key': key,
                              'value': file_1[key]})
        elif file_1[key] == file_2[key]:
            diff_tree.append({'type': 'unchanged', 'key': key,
                              'value': file_1[key]})
        elif isinstance(file_1[key], dict) and isinstance(file_2[key], dict):
            diff_tree.append({'type': 'nested', 'key': key,
                              'value': gen_diff(file_1[key], file_2[key])})
        else:
            diff_tree.append({'type': 'changed', 'key': key,
                              'old_value': file_1[key],
                              'new_value': file_2[key]})
    return diff_tree
