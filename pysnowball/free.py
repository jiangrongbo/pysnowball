"""
自选股
"""
import requests
import json
import pandas as pd
from pysnowball import api_ref, utls

"""
创建自选股分组
"""


def create_free_item(item_name):
    url = api_ref.create_free_item + item_name
    return utls.post(url)


"""
删除自选股分组
"""


def remove_free_item(pids):
    url = api_ref.remove_free_item + pids
    return utls.post(url)


"""
查询所有自选股分组
"""


def list_free_item():
    url = api_ref.list_free_item
    result = utls.fetch(url)
    stock_list = result['data']['stocks']
    return pd.DataFrame(stock_list)


"""
pnames 分组名称
symbols 股票代码
添加股票到分组
"""


def add_stock_to_item(pnames, symbols):
    url = api_ref.add_stock_to_item + '?pnames=' + pnames + '&symbols=' + symbols
    return utls.post(url)


"""
关注股票
"""


def subscribe_stock(stock_code):
    cookies = {
        'device_id': 'd5836b07dd86cfd920118dc61b71590a',
        'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1630738258',
        'remember': '1',
        'xq_a_token': 'a258ff0bd31b6a67131e6e8cd1cdba947d22b960',
        'xqat': 'a258ff0bd31b6a67131e6e8cd1cdba947d22b960',
        'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjY0MDA5MjYyMzIsImlzcyI6InVjIiwiZXhwIjoxNjMzMzMwMjkwLCJjdG0iOjE2MzA3MzgyOTA1NzMsImNpZCI6ImQ5ZDBuNEFadXAifQ.oKMNQyvQgeuh07BVGjFzmX7JSNdLQoTF7mm-KV3tfF6ryAO46zmN61u1WYqM46gMfcJ_UOtibl7ejLGvl7YqIAGAm7q-CtpmTdUJvU7MeXe4uRGAefuFfohCTzT8viVPUGKXWshyaldyMYw8qpAiQ42X_gSYfarsRRWclx7RTsPxDGVLl6rdRyDmcK7Cq1kbOiUmVqKUwojVpGmj_A4f6ooGjLTAFU7FdzFEy0dpY1vjFa60qBqpioWN6TqD82sJ1Q3Pzpsy-Ywm-HzFrCyXoeUKOgUk2frUzsGwq0PFwrOqRbCAGEIxN5nI3A7qoGifVu_r_RZ5yMIa2IZCuUEzsQ',
        'xq_r_token': '1a1a4e81bc05538fcc70219cede275920882ae2b',
        'xq_is_login': '1',
        'u': '6400926232',
        's': 'dv1cvdfzcc',
        'bid': 'b9acfd50efe6eeca7eb8ea629d70ba11_kt5fheea',
        '__utmc': '1',
        '__utmz': '1.1630738307.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utma': '1.827161833.1630738307.1630738307.1630740118.2',
        '__utmb': '1.5.10.1630740118',
        'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1630740856',
        'acw_tc': '2760829216307419251272125eb7b92549e13cd670b1012a6f4d3239f355f5',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4621.4 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'cache-control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"macOS"',
        'Origin': 'https://xueqiu.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xueqiu.com/hq',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {
        'symbols': stock_code
    }

    response = requests.post('https://xueqiu.com/service/v5/stock/portfolio/stock/add', headers=headers,
                             cookies=cookies, data=data)
    if response.status_code != 200:
        raise Exception(response.content)

    return json.loads(response.content)


"""
修改自选股分组
"""


def modify_portfolio(symbols, pnames, category):
    cookies = {
        'device_id': 'd5836b07dd86cfd920118dc61b71590a',
        'remember': '1',
        'xq_a_token': 'a258ff0bd31b6a67131e6e8cd1cdba947d22b960',
        'xqat': 'a258ff0bd31b6a67131e6e8cd1cdba947d22b960',
        'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjY0MDA5MjYyMzIsImlzcyI6InVjIiwiZXhwIjoxNjMzMzMwMjkwLCJjdG0iOjE2MzA3MzgyOTA1NzMsImNpZCI6ImQ5ZDBuNEFadXAifQ.oKMNQyvQgeuh07BVGjFzmX7JSNdLQoTF7mm-KV3tfF6ryAO46zmN61u1WYqM46gMfcJ_UOtibl7ejLGvl7YqIAGAm7q-CtpmTdUJvU7MeXe4uRGAefuFfohCTzT8viVPUGKXWshyaldyMYw8qpAiQ42X_gSYfarsRRWclx7RTsPxDGVLl6rdRyDmcK7Cq1kbOiUmVqKUwojVpGmj_A4f6ooGjLTAFU7FdzFEy0dpY1vjFa60qBqpioWN6TqD82sJ1Q3Pzpsy-Ywm-HzFrCyXoeUKOgUk2frUzsGwq0PFwrOqRbCAGEIxN5nI3A7qoGifVu_r_RZ5yMIa2IZCuUEzsQ',
        'xq_r_token': '1a1a4e81bc05538fcc70219cede275920882ae2b',
        'xq_is_login': '1',
        'u': '6400926232',
        's': 'dv1cvdfzcc',
        'bid': 'b9acfd50efe6eeca7eb8ea629d70ba11_kt5fheea',
        'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1630810020,1630827141,1631276562,1631283655',
        'is_overseas': '0',
        'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1631342173',
    }

    headers = {
        'Host': 'stock.xueqiu.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4628.3 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://xueqiu.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://xueqiu.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    data = 'symbols=' + symbols + '&pnames=' + pnames + '&category=' + category

    response = requests.post('https://stock.xueqiu.com/v5/stock/portfolio/stock/modify_portfolio.json', headers=headers,
                             cookies=cookies, data=data)


"""
查询自选股分组下所有股票
"""


def list_free_stock(pid):

    params = (
        ('category', '1'),
        ('page', '1'),
        ('pid', pid),
        ('size', '2000'),
    )

    url = api_ref.list_free_stock

    result = utls.fetch_with_param(url, params)
    stock_list = result['data']['stocks']
    return pd.DataFrame(stock_list)
