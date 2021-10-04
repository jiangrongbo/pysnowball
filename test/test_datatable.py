import unittest

import pandas as pd
import pysnowball as ball
import datatable as dt

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class DataTableTest(unittest.TestCase):

    def test_datatable(self):
        dt1 = dt.fread("test.csv")
        dt1


if __name__ == '__main__':
    unittest.main()
