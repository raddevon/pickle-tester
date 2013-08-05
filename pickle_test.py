import unittest
from pickler import list_pickler, unpickler
from os import remove


class PicklingTests(unittest.TestCase):

    def test_mixed_pickled_list_matches_original(self):
        test_list = [1, 2, 'red', 'blue']
        with open('testfile.p', 'w') as f:
            list_pickler(test_list, f)
        with open('testfile.p', 'r') as f:
            unpickled = unpickler(f)
        self.assertEqual(test_list, unpickled)

    def test_pickled_list_of_numbers_matches_original(self):
        test_list = [1, 2, 3, 4]
        with open('testfile.p', 'w') as f:
            list_pickler(test_list, f)
        with open('testfile.p', 'r') as f:
            unpickled = unpickler(f)
        self.assertEqual(test_list, unpickled)

    def test_pickled_list_of_strings_matches_original(self):
        test_list = ['one', 'two', 'three', 'four']
        with open('testfile.p', 'w') as f:
            list_pickler(test_list, f)
        with open('testfile.p', 'r') as f:
            unpickled = unpickler(f)
        self.assertEqual(test_list, unpickled)

    def tearDown(self):
        remove('testfile.p')
