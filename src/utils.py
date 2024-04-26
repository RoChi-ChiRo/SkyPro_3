import json
import datetime
import os.path
from config import ROOT_DIR


def read_operations(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def format_operation(operation):
    output_str = ''
    date = datetime.datetime.fromisoformat(operation.get('date'))
    output_str += date.__format__('%d.%m.%Y ')
    output_str += operation.get('description\n')


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

    return operations[:num]
