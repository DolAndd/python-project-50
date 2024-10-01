import json
import yaml

YAML_FORMAT = ('.yml', '.yaml')
JSON_FORMAT = '.json'


def check_format_file(pathfile):
    if pathfile.endswith(JSON_FORMAT):
        return 'json'
    elif pathfile.endswith(YAML_FORMAT):
        return 'yaml'


def files_parsers(data, file_format):
    if file_format == 'json':
        return json.load(data)
    elif file_format == 'yaml':
        return yaml.load(data, Loader=yaml.FullLoader)


def get_file_data(pathfile):
    data = open(pathfile, 'r')
    return files_parsers(data, check_format_file(pathfile))
