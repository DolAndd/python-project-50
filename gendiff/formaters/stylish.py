def get_tree_from_dict(coll, step):
    string_tree = ''
    if isinstance(coll, dict):
        string_tree += '{\n'
        for key, value in coll.items():
            string_tree += (f"{' ' * (4 * (step + 1))}{key}: "
                            f"{get_tree_from_dict(value, step + 1)}\n")
        string_tree += (' ' * (4 * step)) + '}'
    else:
        string_tree += str(coll)
    return string_tree


def get_stylish_format(sorted_diff):
    def walk(node, depth):
        text = '{\n'
        for k, v in node.items():
            step_depth = ' ' * (4 * depth - 2)
            if v['type'] == 'unchanged':
                text += (f"{step_depth}  {k}: "
                         f"{get_tree_from_dict(v['value'], depth)}\n")
            if v['type'] == 'added':
                text += (f"{step_depth}+ {k}: "
                         f"{get_tree_from_dict(v['value'], depth)}\n")
            if v['type'] == 'removed':
                text += (f"{step_depth}- {k}: "
                         f"{get_tree_from_dict(v['value'], depth)}\n")
            if v['type'] == 'changed':
                text += (f"{step_depth}- {k}: "
                         f"{get_tree_from_dict(v['old_value'], depth)}\n")
                text += (f"{step_depth}+ {k}: "
                         f"{get_tree_from_dict(v['new_value'], depth)}\n")
            if v['type'] == 'nested':
                text += (f"{step_depth}  {k}: "
                         f"{walk(v['value'], depth + 1)}\n")
        return text + f"{' '*(4*depth-4)}" + '}'
    return walk(sorted_diff, 1)
