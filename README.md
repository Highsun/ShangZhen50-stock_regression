# ShangZheng50-stock_regression

一次多元统计分析的小组作业。

于 2024.12.16 已完结。

## IDEA

+ 以上证指数为 $ y $ ，基于经济学理论选取若干对上证指数具有较大影响力的因子 $ x_1 \sim x_n $ ：
  + 股票类
    + 标普500 $ \Delta $
    + 布伦特原油当月连续 $ * $ $ \Delta $
    + 恒生指数
    + 沪深300
    + 黄金美元价格 $ * $ $ \Delta $
    + 科创50
    + 美元指数
    + 纳斯达克 $ \Delta $
    + 中国黄金 $ * $ $ \Delta $
    + 中证A100
    + USDCNH $ * $ $ \Delta $
    + USDCNY $ * $ $ \Delta $
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
+ 根据各类数据的特点，分别选取不同的回归模型进行分析：
  
  | 因子类别     | 简单线性回归 | LASSO | VAR/VECM | 时间序列模型 | 非线性模型   |
  | ------------ | ------------ | ----- | -------- | ------------ | ------------ |
  | 股票类       | ✔            | ✔     | ✔        | ARIMA/ARCH   | SVR/神经网络 |
  | 汇率类       | ✔            | ✔     | ✔        | ARIMA/VECM   | 树模型       |
  | CPI类        | ✔            | ✔     |          |              | 贝叶斯回归   |
  | 宏观经济指标 | ✔            | ✔     | ✔        | 动态因子模型 | 分位数回归   |
+ 评价指标：MAE、MSE等
+ 预测实验、结果可视化等

## Changelog

### v1.0.0 - 2024.12.11

+ 基于经济学理论收集了各类、若干与上证指数有较大关联性的数据，并进行分类。

+ 对收盘价：以上证指数为 $ y $ ，各股票类数据为 $ x $ ，进行单变量线性回归分析，绘制出了拟合效果较好的部分图像，存储于 `main/ouput/lr` 。部分效果欠佳的绘图结果未做保留，在 **IDEA** 部分以 “$ * $” 符号标注，留待后续进一步分析。

### v1.1.0 - 2024.12.12

+ 完成了一些基础图像的绘制，存储于 `main/output/display` ：

  + 人民币汇率中间价


  + USDCNH和USDCNY对比图

  + 上证指数收盘价


### v1.2.0 - 2024.12.13

+ 对收盘价：以上证指数为 $ y $ ，各股票类数据为 $ x $ ，进行单因素 LASSO 回归分析，绘制出了拟合效果较好的部分图像，存储于 `main/ouput/lasso` 。部分效果欠佳的绘图结果未做保留，在 **IDEA** 部分以 “$ \Delta $” 符号标注，简要原因分析：LASSO 回归除了均方误差外，还引入了一个模型系数的 L1 范数作为正则化项，这导致 LASSO 回归会强迫某些特征的系数缩小甚至变为0以使得总损失最小化，但这也恰恰导致了在单因素 LASSO 回归分析中，部分在线性回归中尚有良好表现的特征在 LASSO 回归中被大幅度压缩。
+ 以上证指数收盘价为 $ y $ ，其余各列数据为 $ X $ ，进行多因素线性回归，并基于收盘价外的数据对收盘价进行预测。
+ 以上证指数收盘价为 $ y $ ，选取单因素线性回归效果较好的五只股票为 $ X $ ，进行多因素线性回归，并基于这五只股票的数据对收盘价进行预测。

### v1.3.0 - 2024.12.16

+ 利用 OLS summary 工具对线性回归结果进行分析，所有股票类因素和上证指数的分析结果均予以保留，存储于 `main/output/OLS` 。
+ 实验报告由 Maxence 撰写并已添加到项目中。

---

Created and edited by **Highsun**, last update: **2024.12.16**

Any questions please contact me by email: highsun910@gmail.com