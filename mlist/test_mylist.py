import unittest
from mlist import MLista


class TestMLista(unittest.TestCase):

    def test_construct(self):
        my_list = MLista(2)
        self.assertEqual(my_list._capacity, 2)
        self.assertEqual(my_list._list, [])

    def test_add_element(self):
        my_list = MLista(1)
        result = my_list.add_element(2)
        self.assertTrue(result)
        result = my_list.add_element(5)
        self.assertFalse(result)

    def test_get_index(self):
        my_list = MLista(4)
        my_list.add_element(5)
        my_list.add_element(2)
        my_list.add_element(9)
        my_list.add_element(1)
        result = my_list.get_index(2)
        self.assertEqual(result, 1)
        result = my_list.get_index(10)
        self.assertEqual(result, -1)

    def test_get_element(self):
        my_list = MLista(3)
        my_list.add_element(2)
        my_list.add_element(5)
        my_list.add_element(1)
        result = my_list.get_element(2)
        self.assertEqual(result, 1)
        result = my_list.get_element(4)
        self.assertEqual(result, -1)

    def test_get_length(self):
        my_list = MLista(4)
        my_list.add_element(3)
        my_list.add_element(7)
        my_list.add_element(2)
        result = my_list.get_length()
        self.assertEqual(result, 3)

    def test_get_capacity(self):
        my_list = MLista(5)
        my_list.add_element(0)
        result = my_list.get_capacity()
        self.assertEqual(result, 5)

    def test_remove_duplicates(self):
        my_list = MLista(3)
        my_list.add_element(3)
        my_list.add_element(3)
        my_list.add_element(3)
        result = my_list.remove_duplicates(3)
        self.assertEqual(result, [3])
        my_list.add_element(2)
        result = my_list.remove_duplicates(2)
        self.assertEqual(result, [3, 2])

    def test_reverse(self):
        my_list = MLista(3)
        my_list.add_element(1)
        my_list.add_element(2)
        my_list.add_element(3)
        result = my_list.reverse()
        self.assertEqual(result, [3, 2, 1])

    def test_increase_capacity(self):
        my_list = MLista(0)
        result = my_list.increase_capacity(1)
        self.assertTrue(result)
        result = my_list.increase_capacity(-1)
        self.assertFalse(result)
        result = my_list.increase_capacity(0)
        self.assertFalse(result)

    def test_reduce_capacity(self):
        my_list = MLista(1)
        result = my_list.reduce_capacity(1)
        self.assertTrue(result)
        result = my_list.reduce_capacity(-1)
        self.assertFalse(result)
        result = my_list.reduce_capacity(5)
        self.assertFalse(result)
