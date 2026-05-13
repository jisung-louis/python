import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanfont

df = pd.read_csv(
    './naebupyeongga/data/books.csv',
    encoding='utf-8',
    header=0
)

df.info()
print(df.head(10))
print()


# ================ [2] 전처리 ================

# 1. 가격데이터 전처리
# 크롤링할 때부터 되어있음

# 2. 출판년월 데이터 전처리
# print(df['출판년월'])
df['출판년월'] = pd.to_datetime(df['출판년월'], format="%Y년 %m월")
df['출판년'] = df['출판년월'].dt.year
df['출판월'] = df['출판년월'].dt.month
# print(df['출판년월'])
# print()
# print(df['출판년'])
# print()
# print(df['출판월'])


# ================ [3] 기본 통계 분석 ================

# 1. 가격 통계 분석
# 1-가. 평균 가격 계산
print('[평균가격] : ', df['가격'].mean())
# 1-나. 최고 가격 계산
print('[최고가격] : ', df['가격'].max())
# 1-다. 최저 가격 계산
print('[최저가격] : ', df['가격'].min())

# 2. 출판년도 분석
# 2-가. 연도별 도서 수 계산
print(df['출판년'].value_counts())


# ================ [4] 데이터 시각화 기능 ================

# 1. 가격 분포 시각화
# 1-가. 히스토그램 구현
# 1-나. 가격대별 도서 개수 출력
# 1-다. 그래프 제목 및 축 이름 출력
plt.hist(df['가격'], bins=10, color='skyblue', alpha=0.7)
plt.title('가격 분표 히스토그램')
plt.xlabel("가격")
plt.ylabel("도서 수")
plt.show()

# 2. 출판년도별 도서 수 시각화
# 2-가. 막대그래프 구현
# 2-나. 연도별 출판 도서 수 출력
# 2-다. 그래프 제목 및 축 이름 출력
sns.countplot(data=df, x='출판년')
plt.title("연도별 출판 도서")
plt.xlabel("출판년도")
plt.ylabel("도서 수")
plt.show()

print()
print(df['가격'].mean())
print(df['가격'].max())
print(df['가격'].min())
print(df['출판년'].value_counts().index[0])

