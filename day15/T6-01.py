import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import koreanfont

# [0. 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster
# https://www.kaggle.com/competitions/titanic/overview

# [1. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# [2. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.

# [3. 데이터 시각화 및 분석]
# 3-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
# 3-2 : 연령대별 상세 분석: 나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다. 데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
# 3-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# 3-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# 3-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.

# [1] csv 불러오기
df = pd.read_csv(
    './day15/train.csv',
    on_bad_lines='warn',
    usecols=['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'Embarked']
)

print(df.head())
print()

df.info()
print()

print(df.isnull().sum())
print()

# [2] 데이터 전처리
df['Age'] = df['Age'].fillna( df['Age'].median() )
df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode()[0] )
print(df.isnull().sum())

# [3] 데이터 시각화
# plt.bar : 수치값 (남 : 3 , 여 : 5)  vs  sns.countplot : 범주값 (남남남여여여여여)
# 3-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
sns.countplot(data=df, x='Survived')
plt.title('생존 여부 분포')
plt.xlabel('생존여부 0:사망 1:생존')
plt.xticks([0,1], ['사망', '생존'])
plt.ylabel('인원 수')
plt.show()

# 3-2 : 연령대별 상세 분석: 나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다. 데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.

print(df[df['Survived'] == 0]['Age'])
print(df[df['Survived'] == 1]['Age'])

sns.histplot(df[df['Survived'] == 0]['Age'], label='사망', color='#FF0000', kde=True)
sns.histplot(df[df['Survived'] == 1]['Age'], label='생존', color='#0000FF', kde=True)

plt.title('나이별 생존 분포')
plt.xlabel('나이')
plt.ylabel('인원수')
plt.legend()
plt.show()

# 3-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df, x='Sex', hue='Survived')
plt.legend(title='범례제목', labels=['사망', '생존'])
plt.show()

# 3-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.legend(title='범례제목', labels=['사망', '생존'])
plt.show()
# 3-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df, x='Embarked', hue='Survived')
plt.legend(title='범례제목', labels=['사망', '생존'])
plt.show()