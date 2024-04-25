import json


def read_operations(path):
    with open(path) as file:
        data = file.read()
        return json.dumps(data)


def format_operation(operation):
    pass


def get_last_operations(num=5):
    pass
