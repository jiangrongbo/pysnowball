import unittest

import pandas as pd
import pysnowball as ball

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class ScreenerTest(unittest.TestCase):

    def test_list_industries(self):
        print(ball.list_industries())

    def test_screener(self):
        ball.set_token('xq_a_token=f8e9ce5454e5b3d58d5a981d1657177c72665885;')
        screener_df = ball.screener()
        print(screener_df)
        # screener_df.to_csv('stock20210918.csv')

    def test_list_stock(self):
        stock_df = ball.list_stock();
        print(stock_df)
        pass


if __name__ == '__main__':
    unittest.main()