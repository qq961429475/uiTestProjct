import os

import yaml
from jsonpath import jsonpath

from config.filepath import case_data_path


def read_yaml(filename):
    filepath = os.path.dirname(os.path.dirname(__file__))
    with open(filepath + '/data/' + filename, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return data


def load_case_data(filename):
    for root, dirs, files in os.walk(case_data_path):
        try:
            for file in files:
                if file.endswith('.yaml') and file == filename:
                    with open(root + filename, 'r', encoding='utf-8') as f:
                        data = yaml.load(stream=f, Loader=yaml.FullLoader)
                        return data, jsonpath(data, '$..case_description')
                else:
                    filename = filename + '.yaml'
                    if file.endswith('.yaml') and file == filename:
                        with open(root + filename, 'r', encoding='utf-8') as f:
                            data = yaml.load(stream=f, Loader=yaml.FullLoader)
                            return data, jsonpath(data, '$..case_description')
        except FileNotFoundError as e:
            raise e


if __name__ == '__main__':
    print(load_case_data('test_01')[0])
