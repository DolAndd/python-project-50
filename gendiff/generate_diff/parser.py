import json
import yaml


def read_json(pathfile):
    return json.load(open(pathfile, 'r'))


def read_yaml(pathfile):
    return yaml.load(open(pathfile, 'r'), Loader=yaml.FullLoader)


def files_parser(pathfile_1):
    json_format = '.json'
    yaml_format = ('.yml', '.yaml')
    if pathfile_1.endswith(json_format):
        return read_json(pathfile_1)
    elif pathfile_1.endswith(yaml_format):
        return read_yaml(pathfile_1)
