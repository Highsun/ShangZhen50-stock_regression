import os
import efinance as ef
import pandas as pd
import akshare as ak
import warnings

# 忽略警告
warnings.filterwarnings('ignore')

# 定义指数名称和目标年份
name = 'iVIX'
target_year = '2024'

# 获取指数的历史行情数据
data = ef.stock.get_quote_history(name)

# 转换日期列为 datetime 格式
data['日期'] = pd.to_datetime(data['日期'])

# 筛选2024年的数据
data_2024 = data[data['日期'].dt.year == int(target_year)]

# 创建"DATA"文件夹（如果不存在）
output_folder = 'DATA'
os.makedirs(output_folder, exist_ok=True)

# 保存筛选后的数据到文件
output_path = os.path.join(output_folder, f"{name}_2024.csv")
data_2024.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"2024年的数据已保存到 {output_path}")

# 获取中国财政收入数据
china_fiscal_revenue_data = ak.macro_china_czsr()

# 确保月份列转换为 datetime 格式（严格按照 'YYYY年MM月份' 格式解析）
china_fiscal_revenue_data['月份'] = pd.to_datetime(
    china_fiscal_revenue_data['月份'].str.replace('年', '-').str.replace('月份', ''),
    format='%Y-%m',
    errors='coerce'
)

# 筛选2024年的数据
china_fiscal_revenue_2024 = china_fiscal_revenue_data[
    china_fiscal_revenue_data['月份'].dt.year == 2024
]

# 保存数据到DATA文件夹
output_path = os.path.join(output_folder, "中国财政收入2024.csv")
china_fiscal_revenue_2024.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"2024年的中国财政收入数据已保存到：{output_path}")