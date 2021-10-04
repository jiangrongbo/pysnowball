import unittest

import pandas as pd
import pysnowball as ball

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class ApiTest(unittest.TestCase):

    def test_token(self):
        print(ball.earningforecast('SZ002027'))
        pass

    def test_create_free_item(self):
        print(ball.create_free_item('1'))
        pass

    def test_add_stock_to_item(self):
        print(ball.add_stock_to_item(4,'000001'))

    def test_list_free_item(self):
        print(ball.list_free_item())


if __name__ == '__main__':
    unittest.main()
