import pandas as pd
import statsmodels.api as sm
import os

if not os.path.exists('../output/OLS'):
    os.makedirs('../output/OLS')

## Load data
df_y = pd.read_csv('../dataset/上证指数_2024.csv')
df_x1 = pd.read_csv('../dataset/恒生指数_2024.csv')
df_x2 = pd.read_csv('../dataset/沪深300_2024.csv')
df_x3 = pd.read_csv('../dataset/科创50_2024.csv')
df_x4 = pd.read_csv('../dataset/美元指数_2024.csv')
df_x5 = pd.read_csv('../dataset/中证A100_2024.csv')

df_y['日期'] = pd.to_datetime(df_y['日期'])
df_x1['日期'] = pd.to_datetime(df_x1['日期'])
df_x2['日期'] = pd.to_datetime(df_x2['日期'])
df_x3['日期'] = pd.to_datetime(df_x3['日期'])
df_x4['日期'] = pd.to_datetime(df_x4['日期'])
df_x5['日期'] = pd.to_datetime(df_x5['日期'])

df_y = df_y.rename(columns={'收盘': '上证指数'})
df_x1 = df_x1.rename(columns={'收盘': '恒生指数'})
df_x2 = df_x2.rename(columns={'收盘': '沪深300'})
df_x3 = df_x3.rename(columns={'收盘': '科创50'})
df_x4 = df_x4.rename(columns={'收盘': '美元指数'})
df_x5 = df_x5.rename(columns={'收盘': '中证A100'})

data = pd.merge(df_y[['日期', '上证指数']], df_x1[['日期', '恒生指数']], on='日期', how='inner')
data = pd.merge(data, df_x2[['日期', '沪深300']], on='日期', how='inner')
data = pd.merge(data, df_x3[['日期', '科创50']], on='日期', how='inner')
data = pd.merge(data, df_x4[['日期', '美元指数']], on='日期', how='inner')
data = pd.merge(data, df_x5[['日期', '中证A100']], on='日期', how='inner')

y = data['上证指数']
X = data[['恒生指数', '沪深300', '科创50', '美元指数', '中证A100']]
X = sm.add_constant(X)

## OLS
model = sm.OLS(y, X)
results = model.fit()

# print(results.summary())
output_path = '../output/OLS/OLS_summary-上证指数_多变量.txt'
with open(output_path, 'w') as f:
    f.write(results.summary().as_text())
