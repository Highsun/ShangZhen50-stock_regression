import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

if not os.path.exists('../output/lasso_n'):
    os.makedirs('../output/lasso_n')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load data
df_y = df_y = pd.read_csv('../dataset/上证指数_2024.csv')

def self(df):
    df['日期'] = pd.to_datetime(df['日期'])
    y = df['收盘'].values
    X = df.drop(columns=['日期', '股票名称', '股票代码', '收盘']).values
    return y, X

y, X = self(df_y)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

## lasso regression
lasso = LassoCV(cv=5, random_state=42)
lasso.fit(X_scaled, y)

## visualization
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], y, color='black', label='真实数据')
plt.plot(X_scaled[:, 0], lasso.predict(X_scaled), color='blue', linewidth=3, label='Lasso拟合')
plt.title('Lasso Regression: 上证指数预测')
plt.xlabel('第一个特征')
plt.ylabel('收盘价 (上证指数)')
plt.legend()
plt.show()