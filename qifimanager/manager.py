import datetime
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def mergex(dict1, dict2):
    dict1.update(dict2)
    return dict1


a = pymongo.MongoClient('mgdb').quantaxis.history
a.create_index([("account_cookie", pymongo.ASCENDING),
                ("trading_day", pymongo.ASCENDING)], unique=True)


def promise_list(value):
    return value if isinstance(value, list) else [value]


def get_allaccountname():
    return list(set([i['account_cookie'] for i in a.find({}, {'account_cookie': 1, '_id': 0})]))


def get_historyassets(account_cookie='KTKSt04b_a2009_30min'):
    b = [(item['accounts']['balance'], item['trading_day']) for item in a.find(
        {'account_cookie': account_cookie}, {'_id': 0, 'accounts': 1, 'trading_day': 1})]
    res = pd.DataFrame(b, columns=['balance', 'trading_day'])
    res = res.assign(datetime=pd.to_datetime(
        res['trading_day'])).set_index('datetime').sort_index()
    res = res.balance
    res.name = account_cookie
    return res.drop_duplicates().loc['2020-02-02':]


def get_historytrade(account_cookie='KTKSt04b_a2009_30min'):
    b = [item['trades'].values() for item in a.find(
        {'account_cookie': account_cookie}, {'_id': 0, 'trades': 1, 'trading_day': 1})]
    i = []
    for ix in b:
        i.extend(list(ix))
    res = pd.DataFrame(i)
    res = res.assign(account_cookie=res.user_id, code=res.instrument_id,
                     tradetime=res.trade_date_time.apply(lambda x:  datetime.datetime.fromtimestamp(x/1000000000))).set_index(['tradetime', 'code']).sort_index()
    return res.drop_duplicates().sort_index()


def get_sharpe(n):

    return ((n.iloc[-1]/n.iloc[0] - 1)/len(n)*365)/abs((n.pct_change()*100).std())


def rankstrategy(code):
    res = pd.concat([get_historyassets(i) for i in code], axis=1)
    res = res.fillna(method='bfill').ffill()
    rp = (res.apply(get_sharpe) + res.tail(50).apply(get_sharpe) +
          res.tail(10).apply(get_sharpe)).sort_values()

    return rp[rp > 0.5].sort_values().tail(2)


def get_historypos(account_cookie='KTKSt04b_a2009_30min'):
    b = [mergex(list(item['positions'].values())[0], {'trading_day': item['trading_day']}) for item in a.find(
        {'account_cookie': account_cookie}, {'_id': 0, 'positions': 1, 'trading_day': 1})]
    res = pd.DataFrame(b)
    res.name = account_cookie

    return res.set_index('trading_day')


def get_lastpos(account_cookie='KTKSt04b_a2009_30min'):
    b = [mergex(list(item['positions'].values())[0], {'trading_day': item['trading_day']}) for item in a.find(
        {'account_cookie': account_cookie}, {'_id': 0, 'positions': 1, 'trading_day': 1})]
    res = pd.DataFrame(b)
    res.name = account_cookie

    return res.iloc[-1]


def get_historymargin(account_cookie='KTKSt04b_a2009_30min'):
    b = [(item['accounts']['margin'], item['trading_day']) for item in a.find(
        {'account_cookie': account_cookie}, {'_id': 0, 'accounts': 1, 'trading_day': 1})]
    res = pd.DataFrame(b, columns=['balance', 'trading_day'])
    res = res.assign(datetime=pd.to_datetime(
        res['trading_day'])).set_index('datetime').sort_index()
    res = res.balance
    res.name = account_cookie
    return res
