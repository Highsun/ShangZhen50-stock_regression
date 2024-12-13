import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

if not os.path.exists('../output/mlr'):
    os.makedirs('../output/mlr')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load data
df_y = pd.read_csv('../dataset/上证指数_2024.csv')
df_x1 = pd.read_csv('../dataset/恒生指数_2024.csv')
df_x2 = pd.read_csv('../dataset/沪深300_2024.csv')
df_x3 = pd.read_csv('../dataset/科创50_2024.csv')
df_x4 = pd.read_csv('../dataset/美元指数_2024.csv')
df_x5 = pd.read_csv('../dataset/中证A100_2024.csv')

def df_self(df_y):
    title = '上证指数自回归'
    y = df_y['收盘']
    X = df_y.drop(columns=['收盘', '日期', '股票名称', '股票代码'])
    return X, y, title

import pandas as pd

def stocks(df_y, df_x1, df_x2, df_x3, df_x4, df_x5):
    title = '股票类收盘价'
    X = pd.concat([df_x1['收盘'], df_x2['收盘'], df_x3['收盘'], df_x4['收盘'], df_x5['收盘']], axis=1)
    X.columns = ['恒生指数', '沪深300', '科创50', '美元指数', '中证A100']

    df_y['日期'] = pd.to_datetime(df_y['日期'])
    X['日期'] = pd.to_datetime(df_x2['日期'])

    data = pd.merge(df_y[['日期', '收盘']], X, on='日期', how='inner')
    y = data['收盘']
    X = data.drop(columns=['日期', '收盘'])

    return X, y, title

# X, y, t = df_self(df_y)
X, y, t = stocks(df_y, df_x1, df_x2, df_x3, df_x4, df_x5)

## Multiple Linear Regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'MSE: {mse}')

# linear regression function
print(f'y = {model.intercept_:.2f} + ', end='')
for i in range(len(model.coef_)):
    print(f'{model.coef_[i]:.2f} * {X.columns[i]} + ', end='')

## Plot
title = '多因素线性回归：' + t

plt.figure(figsize=(10, 5))
plt.plot(y_test.values, '.-', label='实际', color='#4C72B0')
plt.plot(y_pred, '.-', label='预测', color='#AF4F49')
plt.legend()
plt.title(title)
plt.xlabel('天数')
plt.ylabel('收盘价')
plt.grid()
plt.tight_layout()
# plt.show()
plt.savefig(f'../output/mlr/mlr_{title}.png', dpi=300)