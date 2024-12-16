import pandas as pd
import statsmodels.api as sm
import os

if not os.path.exists('../output/OLS'):
    os.makedirs('../output/OLS')

## Load data
df_y = pd.read_csv('../dataset/上证指数_2024.csv')
df_x = pd.read_csv('../dataset/恒生指数_2024.csv')

df_y['日期'] = pd.to_datetime(df_y['日期'])
df_x['日期'] = pd.to_datetime(df_x['日期'])

data = pd.merge(df_y[['日期', '收盘']], df_x[['日期', '收盘']], on='日期', how='inner')
data.rename(columns={'收盘_x': df_y['股票名称'][0], '收盘_y': df_x['股票名称'][0]}, inplace=True)

X = data[df_y['股票名称'][0]]
X = sm.add_constant(X)
y = data[df_x['股票名称'][0]]

## OLS 
model = sm.OLS(y, X)
results = model.fit()

# print(results.summary())
with open(f'../output/OLS/OLS_summary-{df_y['股票名称'][0]}_{df_x['股票名称'][0]}.txt', 'w') as f:
    f.write(results.summary().as_text())