"""
选股
"""

import requests
import json
import pandas as pd
from pysnowball import api_ref, utls

"""
获取全部行业
"""

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


def list_industries() -> pd.DataFrame:
    url = api_ref.list_industries
    result = utls.fetch_without_token(url)
    industries_list = result['data']['industries']
    return pd.DataFrame(industries_list)


def screener(page_num, page_size):
    param = (
        ('pettm', ''),
        ('roediluted', ''),
        ('bps', ''),
        ('pelyr', ''),
        ('npay', ''),
        ('eps', ''),
        ('netprofit', ''),
        ('dy_l', ''),
        ('psr', ''),
        ('pb', ''),
        ('total_revenue', ''),
        ('mc', ''),
        ('fmc', ''),
        ('niota', ''),
        ('oiy', ''),
        ('deal', ''),
        ('follow7d', ''),
        ('deal7dpct', ''),
        ('deal7d', ''),
        ('tweet7dpct', ''),
        ('tweet', ''),
        ('follow7dpct', ''),
        ('follow', ''),
        ('tweet7d', ''),
        ('pct', ''),
        ('pct5', ''),
        ('pct60', ''),
        ('amount', ''),
        ('chgpct', ''),
        ('pct20', ''),
        ('pct120', ''),
        ('pct250', ''),
        ('volume', ''),
        ('current', ''),
        ('volume_ratio', ''),
        ('pct_current_year', ''),
        ('pct10', ''),
        ('tr', ''),
        ('npana', ''),
        ('bc', ''),
        ('np', ''),
        ('npt', ''),
        ('tbc', ''),
        ('bi', ''),
        ('mg', ''),
        ('tbi', ''),
        ('tp', ''),
        ('bp', ''),
        ('psf', ''),
        ('ocps', ''),
        ('upps', ''),
        ('beps', ''),
        ('epsdiluted', ''),
        ('epsweighted', ''),
        ('csps', ''),
        ('prec', ''),
        ('cur', ''),
        ('cl', ''),
        ('nca', ''),
        ('ta', ''),
        ('pay', ''),
        ('inv', ''),
        ('eq', ''),
        ('rec', ''),
        ('li', ''),
        ('ncl', ''),
        ('me', ''),
        ('tl', ''),
        ('ia', ''),
        ('the', ''),
        ('fa', ''),
        ('up', ''),
        ('ca', ''),
        ('goodwill', ''),
        ('bncf', ''),
        ('fcb', ''),
        ('cnr', ''),
        ('incf', ''),
        ('fncf', ''),

        ('category', 'CN'),
        ('exchange', 'sh_sz'),
        ('areacode', ''),
        ('indcode', ''),
        ('order_by', 'symbol'),
        ('order', 'desc'),
        ('page', page_num),
        ('size', page_size),
        ('only_count', '0'),
        ('_', '1630812015527')
    )

    url = api_ref.screener

    result = utls.fetch_with_param(url, params=param)
    stock_list = result['data']['list']
    return pd.DataFrame(stock_list)


def list_stock() -> pd.DataFrame:
    params = (
        ('page', '1'),
        ('size', '50'),
        ('order', 'desc'),
        ('order_by', 'percent'),
        ('market', 'CN'),
        ('type', 'sh_sz'),
        ('_', '1630823720796'),
    )

    result = utls.fetch_with_param(api_ref.list_stock, params=params)
    stock_list = result['data']['list']
    return pd.DataFrame(stock_list)
