import unittest

from workpathapi.helpers import create_params


class TestCreateParams(unittest.TestCase):
    # valid data for function
    valid = {'start_date': '2020-01-01',
             'end_date': '2020-01-02'}

    def test_create_params_all_valid(self):
        # normal behavior
        self.assertEqual(self.valid, create_params(**self.valid),
                         "create_params should return the same dict if input only contains valid data")

    def test_create_params_with_non_valid(self):
        # function should remove key value pairs with value=None
        one_none = dict(self.valid, non_valid=None)
        self.assertEqual(self.valid, create_params(**one_none),
                         "create_params should remove None values")

    def test_create_params_missing_end_date(self):
        # function should raise a ValueError if only start date is provided
        self.assertRaises(ValueError, create_params, start_date='2020-01-01')

    def test_create_params_missing_end_date(self):
        # function should raise a ValueError if only end date is provided
        self.assertRaises(ValueError, create_params, end_date='2020-01-02')
