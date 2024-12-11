import pandas as pd
import os

dataset_path = './dataset'
file_name = '上证指数_2024'
path = os.path.join(dataset_path, file_name + '.csv')

data = pd.read_csv(path)
print(data.head(5))
print(data.info())

