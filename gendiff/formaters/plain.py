def get_changed_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value in ('false', 'true', 'null') or isinstance(value, int):
        return value
    return f"'{value}'"


def get_plain_format(sorted_diff):
    def iner(node, root):
        result_text = ''
        for k, v in node.items():
            if v['type'] == 'added':
                result_text += (f"Property '{root + k}' was added with value: "
                                f"{get_changed_value(v['value'])}\n")
            elif v['type'] == 'removed':
                result_text += f"Property '{root + k}' was removed\n"
            elif v['type'] == 'changed':
                result_text += (f"Property '{root + k}' was updated. "
                                f"From {get_changed_value(v['old_value'])} to "
                                f"{get_changed_value(v['new_value'])}\n")
            elif v['type'] == 'nested':
                result_text += iner(v['value'], f'{root + k}.')
        return result_text
    return (iner(sorted_diff, ''))[:-1]
