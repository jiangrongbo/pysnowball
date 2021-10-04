import requests

"""
('indicator', 'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance')
k线图

"""
def kline():

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
        'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1630809720,1630810020,1630827141,1631276562',
        'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1631276570',
    }

    headers = {
        'Host': 'stock.xueqiu.com',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4628.3 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://xueqiu.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://xueqiu.com/S/SZ002352',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('symbol', 'SZ002352'),
        ('begin', '1631363948623'),
        ('period', 'day'),
        ('type', 'before'),
        ('count', '-284'),
        ('indicator', 'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'),
    )

    response = requests.get('https://stock.xueqiu.com/v5/stock/chart/kline.json', headers=headers, params=params,
                            cookies=cookies)

    print(response)
