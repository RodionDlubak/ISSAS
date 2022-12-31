import unittest

import forward_index
import inverted_index
import search_forward
import search_inverted


class TestForwardIndex(unittest.TestCase):
    def test_forward_index_one(self):
        text = 'Test'
        result = forward_index.forward_index(text)
        self.assertEqual(result, ['test'])

    def test_forward_index_many(self):
        text = 'It was a bright cold day in April'
        result = forward_index.forward_index(text)
        self.assertEqual(result, ['a', 'april', 'bright', 'cold', 'day', 'in', 'it', 'was'])

    def test_forward_index_repeated(self):
        text = 'Winston is Winston'
        result = forward_index.forward_index(text)
        self.assertEqual(result, ['is', 'winston'])

    def test_forward_index_empty(self):
        text = ''
        result = forward_index.forward_index(text)
        self.assertEqual(result, [''])


class TestInvertedIndex(unittest.TestCase):
    def test_inverted_index_one(self):
        text = 'Test'
        result = {
            'testword': ['data_1']
        }
        inverted_index.inverted_index(text, result, 'data_2')
        self.assertEqual(result, {
            'test': ['data_2'],
            'testword': ['data_1']
        })

    def test_inverted_index_many(self):
        text = 'It was a testWord'
        result = {
            'testword': ['data_1']
        }
        inverted_index.inverted_index(text, result, 'data_2')
        self.assertDictEqual(result, {
            'a': ['data_2'],
            'it': ['data_2'],
            'testword': ['data_1', 'data_2'],
            'was': ['data_2']
        })

    def test_inverted_index_none(self):
        text = ''
        result = {
            'testWord': ['data_1']
        }
        inverted_index.inverted_index(text, result, 'data_2')
        self.assertEqual(result, {
            'testWord': ['data_1']
        })


class TestSearchForward(unittest.TestCase):
    def test_search_forward_present_in_one(self):
        index = {
            'data_1': ['some', 'testword', 'word'],
            'data_2': ['notatestword'],
            'data_2': ['test']
        }
        result = search_forward.search_forward(index, 'testword')
        self.assertEqual(result, ['data_1'])

    def test_search_forward_present_in_many(self):
        index = {
            'data_1': ['some', 'testword', 'word'],
            'data_2': ['testword']
        }
        result = search_forward.search_forward(index, 'testword')
        self.assertEqual(result, ['data_1', 'data_2'])

    def test_search_forward_absent(self):
        index = {
            'data_1': ['some', 'notatestword', 'word'],
            'data_2': ['notatestword'],
        }
        result = search_forward.search_forward(index, 'testword')
        self.assertEqual(result, [])


class TestSearchInverted(unittest.TestCase):
    def test_search_inverted_present_in_one(self):
        index = {
            'testword': ['data_1'],
            'notatestword': ['data_2'],
        }
        result = search_inverted.search_inverted(index, 'testword')
        self.assertEqual(result, ['data_1'])

    def test_search_inverted_present_in_many(self):
        index = {
            'testword': ['data_1', 'data_2'],
            'notatestword': ['data_3'],
        }
        result = search_inverted.search_inverted(index, 'testword')
        self.assertEqual(result, ['data_1', 'data_2'])

    def test_search_inverted_absent(self):
        index = {
            'notatestword': ['file2'],
            'notatestword2': ['file2', 'file2'],
        }
        result = search_inverted.search_inverted(index, 'testword')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()