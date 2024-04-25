import json


def read_operations(path):
    with open(path) as file:
        return json.dump(file)


def format_operation(operation):
    pass


def get_last_operations(num=5):
    pass
