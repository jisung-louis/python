# [1. 서울시 공공자전거 대여이력 분석]
# 출처: 서울 열린데이터 광장

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import koreanfont

# [2. 가설]
# 가설 1: 출퇴근 시간대(08시, 18시 전후)의 자전거 대여량이 다른 시간대에 비해 압도적으로 높을 것이다.
# 가설 2: 특정 지하철역 인근이나 유동인구가 많은 지역의 대여소가 대여량 상위권을 차지할 것이다.
# 가설 3: 이용시간과 이용거리 사이에는 강한 양의 상관관계가 존재할 것이다.

# [3. 자료수집]
# 3-1 : https://data.seoul.go.kr/dataList/OA-15182/F/1/datasetView.do
# 3-2 : 2025년 1월, 2월 대여이력 CSV 파일 로드 (encoding='cp949')

# [4. 데이터 전처리 및 병합]
# 4-1 (병합): pd.concat을 사용하여 분리된 월별 데이터를 하나로 통합하고 인덱스를 재부여한다.
# 4-2 (정제): 결측치의 문자열 표현('\N')을 None으로 치환하고, 성별 데이터를 대문자로 통일 및 결측치를 'U'로 보정한다.
# 4-3 (형변환): 이용시간, 거리 등 주요 수치형 변수는 pd.to_numeric으로 변환하고, 날짜 데이터는 pd.to_datetime으로 객체화한다.
# 4-4 (파생변수): 대여일시에서 시간(Hour) 정보를 추출하여 '대여 시간대' 열을 새롭게 생성한다.

# (4-1)
data1 = pd.read_csv(
    './day16/서울특별시 공공자전거 대여이력 정보_2501.csv',
    encoding='cp949'
)
data2 = pd.read_csv(
    './day16/서울특별시 공공자전거 대여이력 정보_2502.csv',
    encoding='cp949'
)

df = pd.concat([data1, data2], ignore_index=True)

df.info()
# print(df.head())
print()

# (4-2) 결측치 확인
print(df.isnull().sum())
# 치환 , df.replace( { 기존값1: 새로운값1, 기존값2: 새로운값2 })
df = df.replace({'\\N': None, '': None})
# 결측치를 U로 보정 , .fillna(보정값)
df['성별'] = df['성별'].str.upper().fillna('U') # U : 성별 알수없음 뜻
print(df.isnull().sum())

# 수치형 문자형 구분하기 위해 df.info() 결과 확인 또는 공식문서 참고
# 대여 대여소번호, 대여거치대, 이용시간(분), 이용거리(M)
# 만약에 .to_numuric() 변환시 오류 발생하면 결측치로 수정 , errors='coerce'
number_cols = ['대여 대여소번호', '반납대여소번호', '이용시간(분)', '이용거리(M)']

for col in number_cols:
    pd.to_numeric(df[col] , errors='coerce').fillna(0)

# 대여일시 , 반납일시 , pd.to_datatime
df['대여일시'] = pd.to_datetime(df['대여일시'])
df['반납일시'] = pd.to_datetime(df['반납일시'])
df['대여 시간대'] = df['대여일시'].dt.hour

df.info() # 전처리 결과 확인

# [5. 데이터 시각화 및 분석]
# 5-1 (성별 분포): sns.countplot을 사용하여 성별에 따른 따릉이 이용 비중을 시각화한다.
sns.countplot(data=df, x='성별')
plt.show()
# 5-2 (시간대 분석): sns.barplot을 사용하여 24시간 중 어느 시간대에 대여가 집중되는지 분석한다.
hour_data = df['대여 시간대'].value_counts().sort_index()   # 대여 시간대별 개수 세기 , 정렬
sns.barplot(x=hour_data.index, y=hour_data.values)
plt.show()
# 5-3 (인기 대여소): value_counts().head(10)를 활용하여 가장 활발한 상위 10개 대여소를 가로 막대 그래프로 시각화한다.
top10 = df['대여 대여소명'].value_counts().head(10)
sns.barplot(x=top10, y=top10.index)
plt.show()
# 5-4 (상관관계): sns.heatmap을 통해 이용시간, 이용거리, 시간대 등 수치 데이터 간의 밀접도를 분석한다.
# df.select_dtypes(include='선택할타입')
number_data = df.select_dtypes(include='number')
matrix = number_data.corr()
sns.heatmap(matrix, cmap='coolwarm', annot=True, linewidths=0.5)
plt.show()