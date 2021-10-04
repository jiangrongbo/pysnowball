import unittest
import os
import pandas as pd
import pysnowball as ball
import numpy as np
from pandasgui import show

# import qgrid
# from pivottablejs import pivot_ui
# import tabloo
# import dash
# import dash_table

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class StockTest(unittest.TestCase):

    def test_batch_query_stock(self):
        symbols = 'SH688027,SZ300363,SH603688,SZ300123,SZ300481,SH688226,SZ300040,SZ300830,SH600259,SH600468,SZ300260,SH688117,SZ300327,SH600490,SH603989,SZ002266,SH603993,SZ300082,SH603160,SH600610,SH603416,SZ002485,SZ300215,SH600667,SZ300638,SZ002706,SZ300972,SH601968,SH688536,SZ300835,SZ002508,SZ002959,SZ000550,SH688533,SZ002214,SH603633,SH688069,SH600460,SH601969,SH603088,SH603661,SZ300239,SH601236,SZ300595,SZ002645,SZ300625,SZ300722,SZ002860,SZ002759,SZ002155'
        batch_query_stock_df = ball.batch_query_stock(symbols)
        print(batch_query_stock_df)
        pass

    def test_list_free_item(self):
        print(ball.list_free_item())

    def test_list_free_stock(self):

        list_free_stock_df = ball.list_free_stock(4)
        print(list_free_stock_df)

    def test_list_free_item_info(self):
        list_free_stock_df = ball.list_free_stock(4)
        list_free_stock_df['assist'] = 1
        # symbols = list_free_stock_df['symbol'].groupby(list_free_stock_df['assist']).agg(','.join).astype(str)

        # print(symbols)
        symbols = ''
        batch_query_stock_df = ball.batch_query_stock(symbols)

        full_stock_info_df = pd.merge(list_free_stock_df, batch_query_stock_df, on='symbol')
        print(full_stock_info_df)

    def test_list_free_stock(self):
        list_free_item_df = ball.list_free_item()
        list_free_item_df = list_free_item_df.query('name == "20210917KDJ"')
        print(list_free_item_df)

        pid = list_free_item_df.iloc[0]['id']

        list_free_stock_df = ball.list_free_stock(pid)

        list_free_stock_df_size = int(list_free_stock_df.shape[0] / 50) + 1

        sub_arys = np.array_split(list_free_stock_df, list_free_stock_df_size)

        tmp_stock_df = pd.DataFrame()
        for sub_list_free_stock_df in sub_arys:
            symbols = ','.join(sub_list_free_stock_df['symbol'].values.tolist())
            batch_query_stock_df = ball.batch_query_stock(symbols)
            tmp_stock_df = tmp_stock_df.append(batch_query_stock_df)

        full_stock_info_df = pd.merge(list_free_stock_df, tmp_stock_df, on='symbol')
        # full_stock_info_df.to_html()
        show(full_stock_info_df, settings={'block': True, 'theme': 'dark'})
        # widget = qgrid.show_grid(full_stock_info_df)
        # pivot_ui(full_stock_info_df)
        # tabloo.show(full_stock_info_df)
        # pprint.pprint(full_stock_info_df)
        # dtale.show(full_stock_info_df)
        # display(full_stock_info_df)

        # app = dash.Dash('test')
        #
        # app.layout = dash_table.DataTable(
        #     id='table',
        #     columns=[{"name": i, "id": i} for i in full_stock_info_df.columns],
        #     data=full_stock_info_df.to_dict('records'),
        # )
        #
        # app.run_server(debug=True)

    def test_query_stock(self):
        print(ball.batch_query_stock('SZ300626'))

    def test_stock_basic(self):
        indicators = {
            'pettm': '市盈率TTM',
            'roediluted': '净资产收益率',
            'bps': '每股净资产',
            'pelyr': '市盈率LYR',
            'npay': '净利润同比增长',
            'eps': '每股收益',
            'netprofit': '净利润',
            'dy_l': '股息收益率',
            'psr': '市销率(倍)',
            'pb': '市净率MRQ',
            'total_revenue': '营业收入',  # total_revenue.20210630
            'mc': '总市值',
            'fmc': '流通市值',
            'niota': '总资产报酬率',
            'oiy': '营业收入同比增长',
            'deal': '累计交易分享数',
            'follow7d': '一周新增关注',
            'deal7dpct': '一周交易分享增长率',
            'deal7d': '一周新增交易分享数',
            'tweet7dpct': '一周讨论增长率',
            'tweet': '累计讨论次数',
            'follow7dpct': '一周关注增长率',
            'follow': '累计关注人数',
            'tweet7d': '一周新增讨论数',
            'pct': '当日涨跌幅',
            'pct5': '近5日涨跌幅',
            'pct60': '近60日涨跌幅',
            'amount': '当日成交额',
            'chgpct': '当日振幅',
            'pct20': '近20日涨跌幅',
            'pct120': '近120日涨跌幅',
            'pct250': '近250日涨跌幅',
            'volume': '本日成交量',
            'current': '当前价',
            'volume_ratio': '当日量比',
            'pct_current_year': '年初至今涨跌幅',
            'pct10': '近10日涨跌幅',
            'tr': '当日换手率',
            'npana': '扣非净利润',
            'bc': '营业成本',
            'np': '归属于母公司所有者的净利润',
            'npt': '净利润',
            'tbc': '营业总成本',
            'bi': '营业收入',
            'mg': '少数股东损益归属于母公司所有者的净利润',
            'tbi': '营业总收入',
            'tp': '利润总额',
            'bp': '营业利润',
            'psf': '每股净资产',
            'ocps': '每股经营现金流',
            'upps': '每股未分配利润',
            'beps': '扣除非经常性损益后的每股收益',
            'epsdiluted': '每股收益',
            'epsweighted': '稀释每股收益',
            'csps': '每股资本公积金',
            'prec': '预收款项',
            'cur': '货币资金',
            'cl': '流动负债',
            'nca': '非流动资产',
            'ta': '资产合计',
            'pay': '应付账款',
            'csps': '资本公积',
            'inv': '存货',
            'eq': '归属于母公司股东权益',
            'rec': '应收账款',
            'li': '长期投资',
            'ncl': '非流动负债',
            'me': '少数股东权益',
            'tl': '负债合计',
            'ia': '无形资产',
            'the': '股东权益合计',
            'fa': '固定资产',
            'up': '未分配利润',
            'ca': '流动资产',
            'goodwill': '商誉',
            'bncf': '经营活动产生的现金流量净额',
            'fcb': '期末现金及现金等价物余额',
            'cnr': '现金及现金等价物净增加额',
            'incf': '投资活动产生的现金流量净额',
            'fncf': '筹资活动产生的现金流量净额'
        }
        stock_basic_df = pd.read_csv('stock20210918.csv', index_col=0)
        stock_basic_df.rename(columns=indicators,inplace=True)
        show(stock_basic_df, settings={'block': True, 'theme': 'dark'})


if __name__ == '__main__':
    unittest.main()
