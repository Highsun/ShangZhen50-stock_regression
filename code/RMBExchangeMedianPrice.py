import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists('../output/display'):
    os.makedirs('../output/display')

## plt config
plt.rcParams['font.sans-serif'] = ['Kaiti SC']
plt.rcParams['axes.unicode_minus'] = False

## Load the data
df = pd.read_csv('../dataset/人民币汇率中间价_2024.csv', index_col='日期')
# print(df.info())

## Convert the exchange rates for indirect quotation currencies
indirect_currencies = [
    '澳元', '林吉特', '卢布', '兰特', '韩元', 
    '迪拉姆', '里亚尔', '福林', '波兰兹罗提', 
    '丹麦克朗', '瑞典克朗', '挪威克朗', '里拉', 
    '比索', '泰铢'
]

for currency in indirect_currencies:
    if currency in df.columns:
        df[currency] = 100 / df[currency]

## Plot the data
x = df.index.to_numpy()
plt.figure(figsize=(10, 8))
for i in df.columns:
    plt.plot(x, df[i], label=i)
plt.xticks(ticks=x[::15], labels=df.index[::15], rotation=45)
plt.title('人民币汇率中间价')
plt.xlabel('日期')
plt.ylabel('中间价')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=7)
plt.tight_layout()
# plt.show()
plt.savefig('../output/display/人民币汇率中间价.png', dpi=300)