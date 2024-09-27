def convert_bool(text):
    if text is True:
        return 'true'
    elif text is False:
        return 'false'
    elif text is None:
        return 'null'
    else:
        return text


def get_tree_value(coll, step):
    string_tree = ''
    if isinstance(coll, dict):
        string_tree += '{\n'
        for key, value in coll.items():
            string_tree += (f"{' ' * (4 * (step + 1))}{key}: "
                            f"{get_tree_value(value, step + 1)}\n")
        string_tree += (' ' * (4 * step)) + '}'
    else:
        string_tree += str(convert_bool(coll))
    return string_tree


def get_stylish_format(sorted_diff):
    def walk(nodes, depth):
        depth_step = ' ' * (4 * depth - 2)
        text = '{\n'
        for node in nodes:
            if node['type'] == 'unchanged':
                text += (f"{depth_step}  {node['key']}: "
                         f"{get_tree_value(node['value'], depth)}\n")
            if node['type'] == 'added':
                text += (f"{depth_step}+ {node['key']}: "
                         f"{get_tree_value(node['value'], depth)}\n")
            if node['type'] == 'removed':
                text += (f"{depth_step}- {node['key']}: "
                         f"{get_tree_value(node['value'], depth)}\n")
            if node['type'] == 'changed':
                text += (f"{depth_step}- {node['key']}: "
                         f"{get_tree_value(node['old_value'], depth)}\n")
                text += (f"{depth_step}+ {node['key']}: "
                         f"{get_tree_value(node['new_value'], depth)}\n")
            if node['type'] == 'nested':
                text += (f"{depth_step}  {node['key']}: "
                         f"{walk(node['value'], depth + 1)}\n")
        return text + f"{' ' * (4 * depth - 4)}" + '}'
    return walk(sorted_diff, 1)
