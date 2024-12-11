# ShangZheng50-stock_regression

一次多元统计分析的小组作业。

## IDEA

+ 以上证指数为 $ y $ ，基于经济学理论选取若干对上证指数具有较大影响力的因子 $ x_1 \sim x_n $ ：
  + 股票类
    + 恒生指数
  + 汇率类
    + 人民币-美元汇率
  + ......
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