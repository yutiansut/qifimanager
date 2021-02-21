# qifi_manager
quantaxis qifi manager

qifi manager is a module for us to manage multi qifi_account slice data in all time scala.

qifi的账户协议被公布在 qifi 项目中: github.com/yutiansut/qifi

本项目可以将 qifi 项目拓展到回测/模拟/实盘的交互之中


Qifi格式的系统会将qifi 协议存储在 quantaxis.history 库中

qifi_manger 分为两个部分


--  qifimanager.manager  对于回测/模拟/实盘等支持qifi协议的账户进行分析


--  qifimanager.qifiwebserver  做为一个微服务把qifi协议的内容提供http端口



### qifimanager.manager


qifimanager分为两个 

-- 管理多个qifi账户的  QA_QIFISMANAGER


-- 管理单个qifi账户，注重于qifi账户本身的分析（风险、绩效）  QA_QIFIMANAGER





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


### qifimanager.qifiwebserver

HTTP API

[GET] http://127.0.0.1:8019/qifis?action=portfoliolist

        {"res": ["factor"]}
    
[GET] http://127.0.0.1:8019/qifis?action=accountlist

        {"res": ["7a654f23-a72e-4609-8320-e5917657885b", "81b6ec6f-b578-46a3-864c-8fe7220e550c", "310cac7b-c500-42ef-841c-a16a9c889a83", "e66fe358-bb7b-4c29-a769-d6a84da87444", "b6c0230a-6d33-4172-b985-4b38be4a2a87", "439acc4e-54c6-4f86-85e0-5a7269d0001e", "f8c7629a-e795-48fd-a1da-8a55314b11d2", "5af251a4-5603-4d8a-880b-e7d0a323ed7e"]}

[GET] http://127.0.0.1:8019/qifis?action=accountinportfolio&portfolio=factor

        {"res": [{"WithdrawQuota": 100000.0, "available": 4984.252, "balance": 100000.0, "close_profit": 0.0, "commission": 23.7479991913, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 94992.0, "position_profit": 0.0, "pre_balance": 100000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 100000.0, "trading_day": "2018-08-22", "user_id": "7a654f23-a72e-4609-8320-e5917657885b", "withdraw": 0.0}, {"WithdrawQuota": 100000.0, "available": 4984.252, "balance": 100000.0, "close_profit": 0.0, "commission": 23.7479991913, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 94992.0, "position_profit": 0.0, "pre_balance": 100000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 100000.0, "trading_day": "2018-08-22", "user_id": "81b6ec6f-b578-46a3-864c-8fe7220e550c", "withdraw": 0.0}, {"WithdrawQuota": 10000000.0, "available": 432939.832749997, "balance": 10000000.0, "close_profit": 0.0, "commission": 2391.1672363281, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 9564669.0, "position_profit": 0.0, "pre_balance": 10000000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 10000000.0, "trading_day": "2019-12-23", "user_id": "310cac7b-c500-42ef-841c-a16a9c889a83", "withdraw": 0.0}, {"WithdrawQuota": 100000.0, "available": 4984.252, "balance": 100000.0, "close_profit": 0.0, "commission": 23.7479991913, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 94992.0, "position_profit": 0.0, "pre_balance": 100000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 100000.0, "trading_day": "2018-08-22", "user_id": "e66fe358-bb7b-4c29-a769-d6a84da87444", "withdraw": 0.0}, {"WithdrawQuota": 10000000.0, "available": 432939.832749997, "balance": 10000000.0, "close_profit": 0.0, "commission": 2391.1672363281, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 9564669.0, "position_profit": 0.0, "pre_balance": 10000000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 10000000.0, "trading_day": "2019-12-23", "user_id": "b6c0230a-6d33-4172-b985-4b38be4a2a87", "withdraw": 0.0}, {"WithdrawQuota": 100000.0, "available": 4984.252, "balance": 100000.0, "close_profit": 0.0, "commission": 23.7479991913, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 94992.0, "position_profit": 0.0, "pre_balance": 100000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 100000.0, "trading_day": "2018-08-22", "user_id": "439acc4e-54c6-4f86-85e0-5a7269d0001e", "withdraw": 0.0}, {"WithdrawQuota": 10000000.0, "available": 432939.832749997, "balance": 10000000.0, "close_profit": 0.0, "commission": 2391.1672363281, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 9564669.0, "position_profit": 0.0, "pre_balance": 10000000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 10000000.0, "trading_day": "2019-12-23", "user_id": "f8c7629a-e795-48fd-a1da-8a55314b11d2", "withdraw": 0.0}, {"WithdrawQuota": 10000000.0, "available": 432939.832749997, "balance": 10000000.0, "close_profit": 0.0, "commission": 2391.1672363281, "currency": "CNY", "deposit": 0.0, "float_profit": 0.0, "frozen_commission": 0.0, "frozen_margin": 0.0, "frozen_premium": 0.0, "margin": 9564669.0, "position_profit": 0.0, "pre_balance": 10000000.0, "premium": 0.0, "risk_ratio": 0.0, "static_balance": 10000000.0, "trading_day": "2019-12-23", "user_id": "5af251a4-5603-4d8a-880b-e7d0a323ed7e", "withdraw": 0.0}]}

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