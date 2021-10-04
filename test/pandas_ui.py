import os
import pandas as pd
import pysnowball as ball
import numpy as np
from pandasgui import show

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


def show_df_data():
    ball.set_token('xq_a_token=f8e9ce5454e5b3d58d5a981d1657177c72665885;')
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
    print(full_stock_info_df)
    show(full_stock_info_df, settings={'block': True})


if __name__ == '__main__':
    show_df_data()
