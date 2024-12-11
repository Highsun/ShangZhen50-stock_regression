# ShangZheng50-stock_regression

一次多元统计分析的小组作业。

## IDEA

+ 以上证指数为 $ y $ ，基于经济学理论选取若干对上证指数具有较大影响力的因子 $ x_1 \sim x_n $ ：
  + 股票类
    + 标普500
    + 布伦特原油当月连续 $ * $
    + 恒生指数
    + 沪深300
    + 黄金美元价格 $ * $
    + 科创50
    + 美元指数
    + 纳斯达克
    + 中国黄金 $ * $
    + 中证A100
    + USDCNH $ * $
    + USDCNY $ * $
  + 汇率类
    + 人民币-美元汇率
    + 人民币汇率中间价
  + CPI类
    + 美国CPI
    + 中国CPI
  + 其他
    + 中国财政收入
    + 中国贸易顺差
    + 中国社会融资规模增量
    + 中国外汇储备
    + 中国综合PMI
    + 中国GDP
    + 中国M2货币供应年率
    + 中国PPI
+ 对选取出来的影响因子进行特征工程（这一步甚至可以先对选取出来的因子探究相互间的关系，再应用于对上证指数的分析），数据可视化。
+ 选取回归模型：
  + Baseline：$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n$
  + 其他：
    + LASSO
    + Ridge
    + 随机森林
+ LOSS：MAE、MSE等
+ 预测实验、结果可视化等

## Changelog

---

Created and edited by **Highsun**, last update: **2024.12.11**

Any questions please contact me by email: highsun910@gmail.com