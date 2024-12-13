import pandas as pd
import numpy as np
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

if not os.path.exists('../output/lasso_1'):
    os.makedirs('../output/lasso_1')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load data
df_y = pd.read_csv('../dataset/上证指数_2024.csv')
df_x = pd.read_csv('../dataset/恒生指数_2024.csv')

df_y['日期'] = pd.to_datetime(df_y['日期'])
df_x['日期'] = pd.to_datetime(df_x['日期'])
data = pd.merge(df_y, df_x, on='日期', how='inner')
print(data.info())

y = data['收盘_y'].values
X = data['收盘_x'].values

y = y.ravel()
X = X.reshape(-1, 1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

## lasso regression
lasso = LassoCV(cv=5, random_state=42)
lasso.fit(X_scaled, y)

## visualization
title = 'Lasso 回归：' + data['股票名称_x'][0] + '和' + data['股票名称_y'][0]

lasso.coef_ = lasso.coef_ / scaler.scale_
lasso.intercept_ = lasso.intercept_ - np.dot(lasso.coef_, scaler.mean_)
lasso_equation = rf'$f(x) = {lasso.coef_[0]:.2f} x + {lasso.intercept_:.2f}$' 

plt.scatter(X, y, color='blue')
plt.plot(X, lasso.predict(X), color='red')
plt.title(title)
plt.xlabel(data['股票名称_x'][0])
plt.ylabel(data['股票名称_y'][0])
plt.text(X.min(), y.max(), lasso_equation, fontsize=12, color='red', verticalalignment='top', usetex=True)
# plt.show()
plt.savefig(f'../output/lasso_1/lasso_{data["股票名称_x"][0]}_{data["股票名称_y"][0]}.png', dpi=300)