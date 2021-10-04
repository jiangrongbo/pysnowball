import unittest

import pandas as pd
import pysnowball as ball

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class BasicTest(unittest.TestCase):

    def test_tuple(self):
        params = (
            ('category', 'CN'),
            ('exchange', 'sh_sz'),
            ('areacode', ''),
            ('indcode', ''),
            ('order_by', 'symbol'),
            ('order', 'desc'),
            ('page', '1'),
            ('size', '5000'),
            ('only_count', '0'),
            ('current', ''),
            ('pct', ''),
            ('mc', ''),
            ('volume', ''),
            ('_', '1630812015527')
        )

        params2 = (('c', 'hello'))

        params = params + params2
        print(type(params))
        print(params)


if __name__ == '__main__':
    unittest.main()
