import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import koreanfont

# [1] 데이터 불러오기
df = pd.read_csv(
    './day15/train-2.csv',
    on_bad_lines='warn',
    na_values=['NA']
)
print(df.head())
print()

df.info()
print()

# missing = df.isnull().sum()
# missing = missing[missing > 0]

# print(missing.to_string())

# [2] 데이터 전처리 (결측치 처리)

df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].median())
df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].median())
df['GarageYrBlt'] = df['GarageYrBlt'].fillna(df['GarageYrBlt'].median())

print()
print(df.isnull().sum()[df.isnull().sum() > 0])

# [3] 시각화

new_df = df.select_dtypes(include=['number'])

print(new_df.columns.to_list())

matrix = new_df[new_df.columns.to_list()].corr()
sns.heatmap(matrix, cmap='coolwarm')
plt.savefig('./heatmap.png')
plt.title('변수들 간의 상관관계')
plt.show()