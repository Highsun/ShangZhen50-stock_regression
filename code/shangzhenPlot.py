import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists('../output/display'):
    os.makedirs('../output/display')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load the data
df = pd.read_csv('../dataset/上证指数_2024.csv')
df['日期'] = pd.to_datetime(df['日期'])

## visualization
plt.figure(figsize=(12, 6))
plt.plot(df['日期'], df['收盘'], '.-', color='#747092')
plt.title('上证指数收盘价')
plt.xlabel('日期')
plt.ylabel('价格')
plt.legend(['收盘'])
plt.grid(True)
# plt.show()
plt.savefig(f'../output/display/上证指数收盘价.png', dpi=300)