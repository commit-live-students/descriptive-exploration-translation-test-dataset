from unittest import TestCase
import pandas as pd


filepath1 = "./data/test_table.csv"
filepath2 = "./data/user_table.csv"

class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res, pd.DataFrame))
        res = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_merge_dataframe(self):
        from build import csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import csv_to_dataframe, merge_dataframe, dtype_category
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        column_list = ["sex", "country", "source", "device", "browser_language", "ads_channel", "browser", "conversion",
                       "test"]
        res_new = dtype_category(res, column_list)
        self.assertTrue(isinstance(res_new, pd.DataFrame))


    def test_categorical_variable_count(self):
        from build import csv_to_dataframe, merge_dataframe, categorical_variable_count
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        column_list = ["sex", "country", "source", "device", "browser_language", "ads_channel", "browser", "conversion",
                       "test"]
        res_new = categorical_variable_count(res)
        self.assertEqual(res_new, 9)


    def test_var_check(self):
        from build import csv_to_dataframe, merge_dataframe, var_check
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        column_list = ["sex", "country", "source", "device", "browser_language", "ads_channel", "browser", "conversion",
                       "test"]
        res_new = var_check(res, 10)
        self.assertEqual(res_new, [])


