# numpy : 배열 기반 , 공학 수치 계산
# pandas : 테이블 기반 , 전처리/필터링(numpy)

# [1] pandas 설치 : pip install pandas
# [2] import pandas as pd

import pandas as pd
print(pd.__version__)

# series
# 1. 생성
x = [ 10 , 20 , 30 , 40 ] # 리스트
z = pd.Series( x )
print( x )
# 0    10       # 0 ~ 4 : 각 요소들의 인덱스
# 1    20       # 10~50 : 각 요소들의 값
# 2    30
# ~~~~~
# dtype: int64  # 데이터의 타입

# 2. 각 요소들의 라벨 포함하기
y = [ 'a', 'b', 'c', 'd' ]
z = pd.Series(x, index=y)   # index에 라벨(목록) 대입
print(z)

# 3. 딕셔너리 으로 생성
# 파이썬 주요 타입 , [리스트] (튜플) {딕셔너리}
x = { 'aaple' : 1 , 'banana' : 2 , 'cherry' : 3 }
z = pd.Series(x)
print(z)

# 4. 주요 속성 확인
print(z.dtype)      # 타입 반환 , int64
print(z.index)      # 인덱스 반환 , Index()
print(z.values)     # 값 반환 ,
print(z.head())     # .head(n) 상위 n개만 출력(기본값 = 5개)(확인용)
print(z.tail())     # .tail(n) 하위 n개만 출력(기본값 = 5개)(확인용)
print(z.iloc[0])    # .iloc[인덱스번호] , 라벨이 아닌 위치로 조회
print(z.iloc[:])    

# 5. 인덱싱


# 11. 통계
print(z.sum())          # 합계
print(z.mean())         # 평균
print(z.max())          # 최댓값
print(z.min())          # 최솟값
print(z.median())       # 중앙값
print(z.var())          # 분산
print(z.std())          # 표준편차
print(z.count())        # 요수 개수
print(z.value_counts()) # 각 요소별 중복 개수
print(z.value_counts(normalize=True)) # 각 요소가 전체에서 차지하는 비율(0~1)

# 12. 정렬 , 한쪽이 정렬되면 다른쪽이 같이 정렬된다.
# 오름차순 : .sort_index() , sort_values()
# 내림차순 : .sort_index(ascending= False) , .sort_values(ascending= False)
x = z.sort_index()
print(x)
x = z.sort_values()
print(x)

# 13. 그룹 , 
# .groupby( level=0 ).집계함수(), 그룹 이후에 집계중요!
# .groupby( level=0 ).egg( ['함수명', '함수명'] )
z = pd.Series( [10,20,30,10,20,30], index = ['a', 'b', 'a', 'b', 'a', 'b'] )
print(z.groupby(level=0))
z.groupby(level=0).sum() # 인덱스별 총합계
print(x)

x = z.groupby( level = 0 ).agg( ['sum', 'mean', 'count']) # 여러개 집계함수는 agg 함수로 묶어서 표현
print(x)

