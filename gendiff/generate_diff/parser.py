import json
import yaml


def get_file_data(pathfile):
    file_format = ''
    yaml_format = ('.yml', '.yaml')
    if pathfile.endswith('.json'):
        file_format = 'json'
    elif pathfile.endswith(yaml_format):
        file_format = 'yaml'
    data = open(pathfile, 'r')
    return files_parsers(data, file_format)


def files_parsers(data, file_format):
    if file_format == 'json':
        return json.load(data)
    elif file_format == 'yaml':
        return yaml.load(data, Loader=yaml.FullLoader)
