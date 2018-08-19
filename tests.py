import re
from unittest import TestCase

from pykey import PyKey


class Test(TestCase):
    def test_length(self):
        message = 'Key length is %i although given length is 10.'

        generator = PyKey(length=10)
        for i in range(10):
            key = generator.get()
            self.assertEqual(len(key), 10, message % len(key))

    def test_repeated_error(self):
        # check length when repeated is True
        self.assertRaises(AssertionError, PyKey, length=10, charset='ABCDEF', repeated=False)

    def test_charset(self):
        generator = PyKey(length=10, charset=PyKey.UPPERS)
        different_letters = re.findall('[^A-Z]', generator.get())
        self.assertListEqual(different_letters, [], 'Key contains different letter from given charset')

    def test_all_letter_different(self):
        generator = PyKey(length=10, charset='ABCDEFGHIJ', repeated=False)
        self.assertEqual(len(set(generator.get())), 10)

    def test_adjacent_error(self):
        self.assertRaises(AssertionError, PyKey, length=10, charset='A', adjacent=False)

    def test_adjacent(self):
        generator = PyKey(length=10, charset='AB', adjacent=False, repeated=True)
        key = generator.get()
        adjacent_count = 0

        for index, letter in enumerate(key[1:]):
            if letter == key[index]:
                adjacent_count += 1

        self.assertEqual(adjacent_count, 0)

    def test_prefix(self):
        self.assertRaises(AssertionError, PyKey, length=2, prefix='-PR')

        generator = PyKey(length=10, prefix='OR-')
        for i in range(10):
            key = generator.get()
            self.assertEqual(len(key), 10)
            self.assertEqual(key.find('OR-'), 0)

    def test_suffix(self):
        self.assertRaises(AssertionError, PyKey, length=2, suffix='-PR')

        generator = PyKey(length=10, suffix='-PR')
        for i in range(10):
            key = generator.get()
            self.assertEqual(len(key), 10)
            self.assertEqual(key[-3:], '-PR')
