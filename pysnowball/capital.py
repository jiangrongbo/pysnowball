import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls

"""
融资融券

融资融券数据
"""


def margin(symbol, page=1, size=180):
    url = api_ref.capital_margin_url + symbol
    url = url + '&page=' + str(page)
    url = url + '&size=' + str(size)
    return utls.fetch(url)


"""
大宗交易

大宗交易数据
"""


def blocktrans(symbol, page=1, size=30):
    url = api_ref.capital_blocktrans_url + symbol
    url = url + '&page=' + str(page)
    url = url + '&size=' + str(size)
    return utls.fetch(url)


"""
资金成交分布

获取资金成交分布数据
"""


def capital_assort(symbol):
    url = api_ref.capital_assort_url + symbol
    return utls.fetch(url)


"""
资金流向趋势

获取当日资金流如流出数据，每分钟数据
"""


def capital_flow(symbol):
    url = api_ref.capital_flow_url + symbol
    return utls.fetch(url)


"""
资金流向历史

获取历史资金流如流出数据，每日数据
"""


def capital_history(symbol, count=20):
    url = api_ref.capital_history_url + symbol
    url = url + '&count=' + str(count)
    return utls.fetch(url)
