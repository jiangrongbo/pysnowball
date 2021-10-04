import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls

"""
实时行情
获取某支股票的行情数据
"""


def quotec(symbols):
    url = api_ref.realtime_quote + symbols
    return utls.fetch_without_token(url)


"""
实时分笔

获取实时分笔数据，可以实时取得股票当前报价和成交信息
"""


def pankou(symbol):
    url = api_ref.realtime_pankou + symbol
    return utls.fetch(url)
