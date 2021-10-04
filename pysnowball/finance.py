import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls

"""
现金流量表
"""


def cash_flow(symbol, is_annals=0, count=10):
    url = api_ref.finance_cash_flow_url + symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count=' + str(count)

    return utls.fetch(url)


"""
业绩指标

按年度、季度获取业绩报表数据。
"""


def indicator(symbol, is_annals=0, count=10):
    url = api_ref.finance_indicator_url + symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count=' + str(count)

    return utls.fetch(url)


"""
资产负债表
"""


def balance(symbol, is_annals=0, count=10):
    url = api_ref.finance_balance_url + symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count=' + str(count)

    return utls.fetch(url)


"""
利润表
"""


def income(symbol, is_annals=0, count=10):
    url = api_ref.finance_income_url + symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count=' + str(count)

    return utls.fetch(url)


"""
主营业务构成
"""


def business(symbol, is_annals=0, count=10):
    url = api_ref.finance_business_url + symbol

    if is_annals == 1:
        url = url + '&type=Q4'

    url = url + '&count=' + str(count)

    return utls.fetch(url)
