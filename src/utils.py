import json


def read_operations(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def format_operation(operation):
    pass


def get_last_operations(num=5):
    pass
