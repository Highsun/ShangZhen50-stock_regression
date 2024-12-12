import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists('../output/display'):
    os.makedirs('../output/display')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load the data
df_1 = pd.read_csv('../dataset/USDCNH_2024.csv')
df_2 = pd.read_csv('../dataset/USDCNY_2024.csv')
# print(df_1.info())
# print(df_2.info())

df_1['日期'] = pd.to_datetime(df_1['日期'])
df_2['日期'] = pd.to_datetime(df_2['日期'])

data_df = pd.merge(df_1, df_2, on='日期', how='inner')
print(data_df.info())

## visualization
plt.figure(figsize=(12, 6))
plt.plot(data_df['日期'], data_df['收盘_x'], label='USDCNH')
plt.plot(data_df['日期'], data_df['收盘_y'], label='USDCNY')
plt.title('美元对人民币汇率')
plt.xlabel('日期')
plt.ylabel('收盘价')
plt.legend()
# plt.show()
plt.savefig(f'../output/display/美元对人民币汇率.png', dpi=300)