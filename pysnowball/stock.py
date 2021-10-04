"""
查询股票信息，最大只支持50条
"""
import json

import requests
import pandas as pd
from pysnowball import api_ref, utls


def batch_query_stock(symbols):
    fields = 'current,percent,pt_cy,pe_ttm,market_capital,roe_ttm,income_cagr,net_profit_cagr,turnover_rate,volume,amount,volume_ratio,amplitude,pb,dividend_yield,chg,followers,pe_forecast,ps,pcf,total_shares,float_shares,capital_net_inflows,main_net_inflows,accer,pt5,pt10,pt20,pt60'
    url = api_ref.batch_query_stock + '?' + 'fields=' + fields + '&symbols=' + symbols

    result = utls.fetch(url)
    stock_list = result['data']['items']
    return pd.DataFrame(stock_list)
