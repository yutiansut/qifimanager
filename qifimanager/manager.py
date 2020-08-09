import datetime
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from qaenv import mongo_ip


def mergex(dict1, dict2):
    dict1.update(dict2)
    return dict1


def promise_list(value):
    return value if isinstance(value, list) else [value]


class QA_QIFIMANAGER():
    """
    用于管理单 qifi 的历史交易情况

    --> 对标 QAAccount 的历史回测模式
    --> 需要增加 QARisk/ QAPerformance 部分的支持
    --> 需要增加对于 QAWEBSERVER 部分的支持
    --> 需要增加对于 web 前端部分的支持

    """

    def __init__(self, mongo_ip=mongo_ip, account_cookie='KTKS_t04b_a2009_30min'):
        self.database = pymongo.MongoClient(mongo_ip).quantaxis.history
        self.database.create_index([("account_cookie", pymongo.ASCENDING),
                                    ("trading_day", pymongo.ASCENDING)], unique=True)

        self.account_cookie = account_cookie
        self.assets = self.get_historyassets(account_cookie)
        self.trade = self.get_historytrade(account_cookie)

    def init_account(self, account_cookie):
        self.account_cookie = account_cookie
        self.assets = self.get_historyassets(self.account_cookie)
        self.trade = self.get_historytrade(self.account_cookie)

    @property
    def month_assets(self):
        return self.assets.resample('M').last()

    @property
    def month_assets_profit(self):
        res = pd.concat([pd.Series(self.assets.iloc[0]),
                         self.month_assets]).diff().dropna()
        res.index = res.index.map(str)
        return res

    def promise_list(self, value) -> list:
        return value if isinstance(value, list) else [value]

    def get_allportfolio(self) -> list:
        return list(set([i['portfolio'] for i in self.database.find({}, {'portfolio': 1, '_id': 0})]))

    def get_portfolio_account(self, portfolio) -> list:
        return list(set([i['account_cookie'] for i in self.database.find({'portfolio': portfolio}, {'account_cookie': 1, '_id': 0})]))

    def get_portfolio_panel(self, portfolio) -> pd.DataFrame:
        r = self.get_portfolio_account(portfolio)
        rp = [self.database.find_one({'account_cookie': i}, {
                                     "accounts": 1, 'trading_day': 1, '_id': 0}) for i in r]
        return pd.DataFrame([mergex(i['accounts'], {'trading_day': i['trading_day']}) for i in rp])

    def get_allaccountname(self) -> list:
        return list(set([i['account_cookie'] for i in self.database.find({}, {'account_cookie': 1, '_id': 0})]))

    def get_historyassets(self, account_cookie='KTKS_t04b_a2009_30min', start='1990-01-01', end=str(datetime.date.today())) -> pd.Series:
        b = [(item['accounts']['balance'], item['trading_day']) for item in self.database.find(
            {'account_cookie': account_cookie}, {'_id': 0, 'accounts': 1, 'trading_day': 1})]
        res = pd.DataFrame(b, columns=['balance', 'trading_day'])
        res = res.assign(datetime=pd.to_datetime(
            res['trading_day']), balance=res.balance.apply(round, 2)).set_index('datetime').sort_index()
        res = res.balance
        res.name = account_cookie

        return res.bfill().ffill().loc[start:end]

    def get_historytrade(self, account_cookie='KTKS_t04b_a2009_30min'):
        b = [item['trades'].values() for item in self.database.find(
            {'account_cookie': account_cookie}, {'_id': 0, 'trades': 1, 'trading_day': 1})]
        i = []
        for ix in b:
            i.extend(list(ix))
        res = pd.DataFrame(i)
        res = res.assign(account_cookie=res.user_id, code=res.instrument_id,
                         tradetime=res.trade_date_time.apply(lambda x:  datetime.datetime.fromtimestamp(x/1000000000))).set_index(['tradetime', 'code']).sort_index()
        return res.drop_duplicates().sort_index()

    def get_sharpe(self, n):
        return ((n.iloc[-1]/n.iloc[0] - 1)/len(n)*365)/abs((n.pct_change()*100).std())

    def rankstrategy(self, code):
        res = pd.concat([self.get_historyassets(i) for i in code], axis=1)
        res = res.fillna(method='bfill').ffill()
        rp = (res.apply(self.get_sharpe) + res.tail(50).apply(self.get_sharpe) +
              res.tail(10).apply(self.get_sharpe)).sort_values()

        return rp[rp > 0.5].sort_values().tail(2)

    def get_historypos(self, account_cookie='KTKS_t04b_a2009_30min'):
        b = [mergex(list(item['positions'].values())[0], {'trading_day': item['trading_day']}) for item in self.database.find(
            {'account_cookie': account_cookie}, {'_id': 0, 'positions': 1, 'trading_day': 1})]
        res = pd.DataFrame(b)
        res.name = account_cookie
        return res.set_index('trading_day')

    def get_lastpos(self, account_cookie='KTKS_t04b_a2009_30min'):
        b = [mergex(list(item['positions'].values())[0], {'trading_day': item['trading_day']}) for item in self.database.find(
            {'account_cookie': account_cookie}, {'_id': 0, 'positions': 1, 'trading_day': 1})]
        res = pd.DataFrame(b)
        res.name = account_cookie
        return res.iloc[-1]

    def get_historymargin(self, account_cookie='KTKS_t04b_a2009_30min'):
        b = [(item['accounts']['margin'], item['trading_day']) for item in self.database.find(
            {'account_cookie': account_cookie}, {'_id': 0, 'accounts': 1, 'trading_day': 1})]
        res = pd.DataFrame(b, columns=['balance', 'trading_day'])
        res = res.assign(datetime=pd.to_datetime(
            res['trading_day'])).set_index('datetime').sort_index()
        res = res.balance
        res.name = account_cookie
        return res


if __name__ == "__main__":
    manager = QA_QIFIMANAGER('192.168.2.124')
    #acc = manager.get_allaccountname()
    # print()
    import matplotlib.pyplot as plt
    manager.get_historyassets().plot()
    plt.show()

    r = manager.month_assets_profit
    r.plot.bar()
    plt.show()
    print(r)
