import os.path
import unittest
import src.utils
from config import ROOT_DIR


class FuncsTest(unittest.TestCase):
    def test_read(self):
        self.assertEqual(src.utils.read_operations(os.path.join(ROOT_DIR, 'tests', 'data.json')),
                         [{'1': 'a'}, {'2': 'b'}, {'3': 'c'}])


if __name__ == '__main__':
    unittest.main()

