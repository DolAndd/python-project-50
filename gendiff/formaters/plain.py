def get_changed_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def get_plain_format(sorted_diff):
    def iner(nodes, root):
        result_text = ''
        for node in nodes:
            if node['type'] == 'added':
                result_text += (f"Property '{root + node['key']}' was added with value: "
                                f"{get_changed_value(node['value'])}\n")
            elif node['type'] == 'removed':
                result_text += f"Property '{root + node['key']}' was removed\n"
            elif node['type'] == 'changed':
                result_text += (f"Property '{root + node['key']}' was updated. "
                                f"From {get_changed_value(node['old_value'])} to "
                                f"{get_changed_value(node['new_value'])}\n")
            elif node['type'] == 'nested':
                result_text += iner(node['value'], f'{root + node["key"]}.')
        return result_text
    return (iner(sorted_diff, ''))[:-1]
