import requests

cookies = {
    'device_id': 'd5836b07dd86cfd920118dc61b71590a',
    'remember': '1',
    'xq_is_login': '1',
    'u': '6400926232',
    's': 'dv1cvdfzcc',
    'bid': 'b9acfd50efe6eeca7eb8ea629d70ba11_kt5fheea',
    'snbim_minify': 'true',
    'xq_a_token': 'f8e9ce5454e5b3d58d5a981d1657177c72665885',
    'xqat': 'f8e9ce5454e5b3d58d5a981d1657177c72665885',
    'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjY0MDA5MjYyMzIsImlzcyI6InVjIiwiZXhwIjoxNjM0Nzg3NjAzLCJjdG0iOjE2MzIxOTU2MDM5MTgsImNpZCI6ImQ5ZDBuNEFadXAifQ.ZOE5f4kx3vjNauoc_-8m-3ZmnM8S5Cf-I_zQ9zZ_cBQrpqG0j5-n7XhYtkFtgxI0mAJcwOFYWmgUlhbKZWt39HfBFOq_pL3_4IrXcVYEK1kk27dEkAmVE60reQnRtgfZkFveyCumgX93lhPk1eEvlFoUN3y6W1Km6Mbf2Wa9W9sJUdsBw8sC9Oea0HZvvi87cFs9aNHEueWrbxP705bcJFTDtfHycAyA4HjjnunKN0ggNbIr0zxZzLfu3at7JjepTnUFooN7nGRs9UGK94CpX683Cov6Eun6c-6KFW0qYNH_3eH_jVHzT9W52pNgNbgCfzfD3Mm8WrHHt6a1UN6KMA',
    'xq_r_token': 'ba675abcb5be7345403947891cb505ef3630d83f',
    'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1631351095,1631890029,1631971555,1633182494',
    'is_overseas': '0',
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1633311519',
}

headers = {
    'Host': 'stock.xueqiu.com',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.10 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://xueqiu.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://xueqiu.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
}

params = (
    ('size', '1000'),
    ('category', '1'),
    ('pid', '4'),
)

response = requests.get('https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?size=1000&category=1&pid=4', headers=headers, cookies=cookies)
