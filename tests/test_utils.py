import os.path
import unittest
import src.utils
from config import ROOT_DIR


class FuncsTest(unittest.TestCase):
    def test_read(self):
        self.assertEqual(src.utils.read_operations(os.path.join(ROOT_DIR, 'tests', 'data.json')),
                         [{"1": "a", "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
                          {"2": "b", "state": "CANCELED", "date": "2018-08-26T10:50:58.294041"},
                          {"3": "c", "state": "EXECUTED", "date": "2017-08-26T10:50:58.294041"}
                          ])

    def test_get_last_operations(self):
        self.assertEqual(src.utils.get_last_operations(1),
                         [{"1": "a", "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}])


if __name__ == '__main__':
    unittest.main()
