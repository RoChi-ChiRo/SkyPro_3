import os.path
import unittest
import src.utils
from config import ROOT_DIR

test_data1 = [{"1": "a", "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
              {"2": "b", "state": "CANCELED", "date": "2018-08-26T10:50:58.294041"},
              {"3": "c", "state": "EXECUTED", "date": "2017-08-26T10:50:58.294041"}
              ]
test_data2 = [{'data': {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
},
    "res": "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
},
    {"data": {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    },
        "res": "23.03.2018 Открытие вклада\nНет данных -> Счет **2431\n48223.05 руб."}
]


class FuncsTest(unittest.TestCase):
    def test_read(self):
        self.assertEqual(src.utils.read_operations(os.path.join(ROOT_DIR, 'tests', 'data.json')), test_data1)

    def test_get_last_operations(self):
        self.assertEqual(src.utils.get_last_operations(2, os.path.join(ROOT_DIR, 'tests', 'data.json')),
                         [{'1': 'a', 'date': '2019-08-26T10:50:58.294041', 'state': 'EXECUTED'},
                          {'3': 'c', 'date': '2017-08-26T10:50:58.294041', 'state': 'EXECUTED'}]
                         )

    def test_format_operation(self):
        for op in test_data2:
            self.assertEqual(src.utils.format_operation(op['data']), op['res'])


if __name__ == '__main__':
    unittest.main()
