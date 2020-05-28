import unittest

from workpathapi.helpers import create_params, list_to_dataframe


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


class TestDictToDataFrame(unittest.TestCase):
    import pandas as pd

    simple_goals_dict = [{'description': 'Description', 'id': 1},
                         {'description': 'Description', 'id': 2}]
    simple_goals_df = pd.DataFrame(data={'description': ['Description', 'Description'], 'id': [1, 2]})

    def test_dict_list_is_returned(self):
        # output_format='dict'
        self.assertEqual(self.simple_goals_dict,
                         list_to_dataframe(list_to_transform=self.simple_goals_dict, output_format='dict'),
                         "simple_goals_dict should return list of dicts if dict is passed as output format")

        # output_format='json'
        self.assertEqual(self.simple_goals_dict,
                         list_to_dataframe(list_to_transform=self.simple_goals_dict, output_format='json'),
                         "simple_goals_dict should return list of dicts if json is passed as output format")

        # output_format='list'
        self.assertEqual(self.simple_goals_dict,
                         list_to_dataframe(list_to_transform=self.simple_goals_dict, output_format='list'),
                         "simple_goals_dict should return list of dicts if list is passed as output format")

    def test_dataframe_is_returned(self):
        import pandas as pd

        # output_format='DataFrame'
        pd.testing.assert_frame_equal(self.simple_goals_df,
                                      list_to_dataframe(list_to_transform=self.simple_goals_dict, output_format='DataFrame'))

        # output_format='pd.DataFrame'
        pd.testing.assert_frame_equal(self.simple_goals_df,
                                      list_to_dataframe(list_to_transform=self.simple_goals_dict, output_format='DataFrame'))

        # output_format='pandas.DataFrame'
        pd.testing.assert_frame_equal(self.simple_goals_df,
                                      list_to_dataframe(list_to_transform=self.simple_goals_dict, output_format='pandas.DataFrame'))

    def test_value_error(self):
        self.assertRaises(ValueError, list_to_dataframe, list_to_transform=self.simple_goals_dict, output_format='wrong')
