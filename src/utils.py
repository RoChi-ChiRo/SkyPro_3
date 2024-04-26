import json
import os.path
from config import ROOT_DIR


def read_operations(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def format_operation(operation):
    pass


def get_last_operations(num=5):
    # get operations
    operations = read_operations(os.path.join(ROOT_DIR, 'data', 'operations.json'))

    # filter
    operations_filtered = []
    for operation in operations:
        if operation.get['state'] == 'EXECUTED':
            operations_filtered.append(operation)
    operations = operations_filtered

    # sort
    def get_date(op):
        return op.get('date')

    operations.sort(key=get_date, reverse=True)
