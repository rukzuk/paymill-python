__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest


from paymill.models.filter import Filter
from paymill.models.filter import FilterList


class TestFilter(unittest.TestCase):
    """

    Testing all methods of the Filter abstraction

    """

    def setUp(self):
        self.filter = Filter('payment', values=('pay_2f82a672574647cd911d',), operator=Filter.OPERATOR['EQUAL'])

    def test_filter_init(self):
        f = Filter('test', values=('test_id', 'test_id'), operator=Filter.OPERATOR['INTERVAL'])
        self.assertIsInstance(f, Filter)

    def test_filter_init_sets_key(self):
        self.assertEqual('payment', self.filter.key)

    def test_filter_init_sets_values(self):
        self.assertEqual(('pay_2f82a672574647cd911d', ), self.filter.values)

    def test_filter_init_sets_operator(self):
        self.assertEqual(Filter.OPERATOR['EQUAL'], self.filter.operator)

    def test_filter_equal_to_dict(self):
        self.assertEqual(dict(payment='pay_2f82a672574647cd911d'), self.filter.to_dict())

    def test_filter_interval_to_dict(self):
        f = Filter('test_interval', values=('123456789', '98717171',), operator=Filter.OPERATOR['INTERVAL'])
        self.assertEqual(dict(test_interval='123456789-98717171'), f.to_dict())

    def test_filter_list(self):
        f1 = Filter('a', values=('1',), operator=Filter.OPERATOR['EQUAL'])
        f2 = Filter('b', values=('2',), operator=Filter.OPERATOR['EQUAL'])
        combined = FilterList(f1, f2)
        self.assertEqual(dict(a='1', b='2'), combined.to_dict())

    def test_equals(self):
        f1 = Filter('a', values=('1',), operator=Filter.OPERATOR['EQUAL'])
        other_key = Filter('b', values=('2',), operator=Filter.OPERATOR['EQUAL'])
        eq = Filter('a', values=('1',), operator=Filter.OPERATOR['EQUAL'])
        other_value = Filter('a', values=('2',), operator=Filter.OPERATOR['EQUAL'])
        other_op = Filter('a', values=('2',), operator=Filter.OPERATOR['GREATER_THAN'])

        self.assertEqual(f1, eq)
        self.assertNotEqual(f1, other_key)
        self.assertNotEqual(f1, other_value)
        self.assertNotEqual(f1, other_op)

    def test_wrong_operator(self):
        with self.assertRaises(Filter.IllegalOperator):
            Filter('a', values=('1',), operator='asdf')