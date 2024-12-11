import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

if not os.path.exists('./output/lr'):
    os.makedirs('./output/lr')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load and preprocess data
y_df = pd.read_csv('./dataset/上证指数_2024.csv')
x_df = pd.read_csv('./dataset/恒生指数_2024.csv')

y_df['日期'] = pd.to_datetime(y_df['日期'])
x_df['日期'] = pd.to_datetime(x_df['日期'])

data_df = pd.merge(y_df, x_df, on='日期', how='inner')
# print(data_df.info())

y = data_df['收盘_y'].values
x = data_df['收盘_x'].values

## linear regression
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

## visualization
title = '线性回归：' + data_df['股票名称_x'][0] + '和' + data_df['股票名称_y'][0]
lr_equation = rf'$f(x) = {model.coef_[0][0]:.2f} x + {model.intercept_[0]:.2f}$'

plt.scatter(x, y, color='blue')
plt.plot(x, model.predict(x), color='red')
plt.title(title)
plt.xlabel(data_df['股票名称_x'][0])
plt.ylabel(data_df['股票名称_y'][0])
plt.text(x.min(), y.max(), lr_equation, fontsize=12, color='red', verticalalignment='top', usetex=True)
plt.show()
# plt.savefig(f'./output/lr/lr_{data_df["股票名称_x"][0]}_{data_df["股票名称_y"][0]}.png', dpi=300)