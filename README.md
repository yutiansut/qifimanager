# qifi_manager
quantaxis qifi manager

qifi manager is a module for us to manage multi qifi_account slice data in all time scala.

qifi的账户协议被公布在 qifi 项目中: github.com/yutiansut/qifi

本项目可以将 qifi 项目拓展到回测/模拟/实盘的交互之中


Qifi格式的系统会将qifi 协议存储在 quantaxis.history 库中






回测:

- 获取资金曲线:
get_historyassets(strategyname, start, end)

- 获取仓位:
get_position(strategyname, start, end)

- 获取历史仓位变化(按交易结算统计):
get_historypos

- 获取最新的仓位:
get_lastpos

- 获取历史保证金:
get_historymargin


HTTP API


[GET] http://127.0.0.1:8019/qifi?action=monthprofit
{
"res": {
    "2020-02-03 00:00:00": 51212,
    "2020-02-04 00:00:00": 50602,
    "2020-02-05 00:00:00": 50922,
    "2020-02-06 00:00:00": 50522,
    "2020-02-07 00:00:00": 50442,
    "2020-02-10 00:00:00": 51233,
    "2020-02-11 00:00:00": 51103,
    "2020-02-12 00:00:00": 51123,
    "2020-02-13 00:00:00": 51023,
    "2020-02-14 00:00:00": 50923,
    "2020-02-17 00:00:00": 51073,
    "2020-02-18 00:00:00": 50993,
    "2020-02-19 00:00:00": 51443,
    "2020-02-20 00:00:00": 50573,
    "2020-02-21 00:00:00": 50893,
    "2020-02-24 00:00:00": 50723,
    "2020-02-25 00:00:00": 50843,
    }
}


[GET] http://127.0.0.1:8019/qifi?action=monthprofit
{
    "res": {
        "2020-02-29 00:00:00": -899.0,
        "2020-03-31 00:00:00": 4024.0,
        "2020-04-30 00:00:00": -7704.0,
        "2020-05-31 00:00:00": 136.0,
        "2020-06-30 00:00:00": -1847.0,
        "2020-07-31 00:00:00": 60.0
    }
}

[GET] http://127.0.0.1:8019/qifi?action=historytrade
{
    "res": [
        {
            "commission": 2.0,
            "direction": "SELL",
            "offset": "OPEN",
            "price": 4084.1736,
            "trade_date_time": 1579141800000000000,
            "volume": 1.0,
            "code": "a2009",
            "datetime": "2020-01-16 10:30:00"
        },
        {
            "commission": 2.0,
            "direction": "BUY",
            "offset": "CLOSE",
            "price": 4065.4436,
            "trade_date_time": 1581297600000000000,
            "volume": 1.0,
            "code": "a2009",
            "datetime": "2020-02-10 09:20:00"
        },
    ]
}