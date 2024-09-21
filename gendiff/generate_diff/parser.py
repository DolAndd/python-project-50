import json
import yaml


def read_json(pathfile):
    return json.load(open(pathfile, 'r'))


def read_yaml(pathfile):
    return yaml.load(open(pathfile, 'r'), Loader=yaml.FullLoader)


def files_parser(pathfile_x):
    json_format = '.json'
    yaml_format = ('.yml', '.yaml')
    if pathfile_x.endswith(json_format):
        return read_json(pathfile_x)
    elif pathfile_x.endswith(yaml_format):
        return read_yaml(pathfile_x)
