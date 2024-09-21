def stylish(sorted_diff):
    def walk(node, depth):
        def is_dict(value):
            def iner(coll, step):
                string_tree = ''
                if isinstance(coll, dict):
                    string_tree += '{\n'
                    for key, val in coll.items():
                        string_tree += (f"{' ' * (4 * (step + 1))}{key}: "
                                        f"{iner(val, step + 1)}\n")
                    string_tree += (' ' * (4 * step)) + '}'
                else:
                    string_tree += str(coll)
                return string_tree
            return iner(value, depth)
        text = '{\n'
        for k, v in node.items():
            if v['type'] == 'unchanged':
                text += f"{' '*(4*depth - 2)}  {k}: {is_dict(v['value'])}\n"
            if v['type'] == 'added':
                text += f"{' '*(4*depth - 2)}+ {k}: {is_dict(v['value'])}\n"
            if v['type'] == 'removed':
                text += f"{' '*(4*depth - 2)}- {k}: {is_dict(v['value'])}\n"
            if v['type'] == 'changed':
                text += f"{' '*(4*depth - 2)}- {k}: {is_dict(v['old_value'])}\n"
                text += f"{' '*(4*depth - 2)}+ {k}: {is_dict(v['new_value'])}\n"
            if v['type'] == 'nested':
                text += (f"{' '*(4*depth - 2)}  {k}: "
                         f"{walk(v['value'], depth + 1)}\n")
        return text + f"{' '*(4*depth-4)}" + '}'
    return walk(sorted_diff, 1)
