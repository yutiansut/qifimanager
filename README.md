# qifi_manager
quantaxis qifi manager

qifi manager is a module for us to manage multi qifi_account slice data in all time scala.

qifi的账户协议被公布在 qifi 项目中: github.com/yutiansut/qifi

本项目可以将 qifi 项目拓展到回测/模拟/实盘的交互之中



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
