from pysnowball import api_ref
from pysnowball import utls

"""
机构评级

获取机构评级数据
"""


def report(symbol):
    url = api_ref.report_latest_url + symbol
    return utls.fetch(url)


"""
业绩预告

按年度获取业绩预告数据
"""


def earningforecast(symbol):
    url = api_ref.report_earningforecast_url + symbol
    return utls.fetch(url)
