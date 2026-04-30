import pandas as pd

# 문제 1: 인덱스 불일치와 결측치 처리
# 딕셔너리 데이터 sales = {'mon': 100, 'tue': 200, 'wed': 300}를 Series로 변환하되, 
# 기존 영문 인덱스('mon', 'tue', 'wed')를 한글 인덱스('월', '화', '수')로 
# 변경하는 코드를 작성하고 결과를 출력하시오.
print("\n======== 문제1 ========")
sales = {'mon': 100, 'tue': 200, 'wed': 300}
x = pd.Series(sales)
x = x.rename({'mon': '월', 'tue':'화', 'wed': '수'})
print(x)

# 문제 2: 슬라이싱을 이용한 부분 수정
# data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])에 대하여
# 1. iloc을 사용하여 인덱스 'b'부터 'd'까지의 값을 추출하고 기존 값에 2를 곱하여 수정하시오.
# 2. loc을 사용하여 인덱스 'd'의 값을 100으로 변경한 뒤 전체를 출력하시오.
print("\n======== 문제2 ========")
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
data.iloc[1:4] = data.iloc[1:4] * 2
data.loc['d'] = 100
print(data)

# 문제 3: Series 연결과 중복 인덱스 조회
# s1 = pd.Series([1, 2], index=['a', 'b'])와 s2 = pd.Series([3, 4], index=['a', 'c'])를 
# pd.concat을 사용하여 연결(result)하고, 인덱스 'a'를 loc으로 조회했을 때의 결과를 출력하시오.
print("\n======== 문제3 ========")
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([3, 4], index=['a', 'c'])
conc_s = pd.concat([s1, s2])
print(conc_s.loc['a'])

# 문제 4: 복합 조건을 활용한 데이터 변경
# data = pd.Series([15, 25, 35, 45, 55])에서 값이 30보다 크고 50보다 작은 요소들만 
# 필터링하여 기존 값에 5를 더한 뒤, 최종 배열의 상태를 출력하시오.
print("\n======== 문제4 ========")
data = pd.Series([15, 25, 35, 45, 55])
data[ (data > 30) & (data < 50) ] = data[ (data > 30) & (data < 50) ] + 5
print(data)

# 문제 5: 범주형 데이터의 빈도수 및 비율 분석
# grade = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B']) 데이터에 대하여
# 1. 각 알파벳별 빈도수(value_counts)를 출력하시오.
# 2. 각 알파벳이 차지하는 상대적 비율을 소수점 형태로 출력하시오. (normalize 인자 활용)
print("\n======== 문제5 ========")
grade = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B'])
print(grade.value_counts())
print(grade.value_counts(normalize=True))

# 문제 6: 산술 연산에서의 인덱스 정렬(Alignment)
# s1 = pd.Series([10, 20], index=['a', 'b'])와 s2 = pd.Series([30, 40], index=['b', 'c'])가 있을 때,
# 두 Series를 더한(s1 + s2) 결과를 출력하고 결측치(NaN)가 발생한 위치와 이유를 설명하시오.
print("\n======== 문제6 ========")
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([30, 40], index=['b', 'c'])
print(s1 + s2)
# NaN이 발생한 위치 : a, c
# NaN이 발생한 이유 : 인덱스 이름 기준으로 산술 연산하기 때문에 두 series에 같은 인덱스가 있어야 한다

# 문제 7: 다중 정렬 구현 (Values & Index)
# data = pd.Series([20, 10, 20, 30], index=['d', 'c', 'a', 'b'])에 대하여
# 데이터 값(Values)은 내림차순으로 정렬하고, 값이 같을 경우 인덱스(Index)를 
# 오름차순으로 정렬한 최종 결과를 출력하시오.
print("\n======== 문제7 ========")

data = pd.Series([20, 10, 20, 30], index=['d', 'c', 'a', 'b'])

# 1차정렬 이후에 유지( + ) 하기 위해서, 1차정렬에 kind속성에 'stable' 적용하여 유지할 수 있다.
result = data.sort_index().sort_values(ascending=False, kind='stable')
print(result)

# 정렬을 따로 하는 경우에는 1차 정렬과 2차 정렬 유지 불가능
# sort = data.sort_values(ascending=False)
# print(sort)
# sort = sort.sort_index()
# print(sort)

# 문제 8: 그룹화 및 다중 집계 함수 적용
# data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'B']) 데이터를 
# 인덱스 레벨(level=0) 기준으로 그룹화하여, 합계(sum)와 평균(mean)을 동시에 구하고 출력하시오.
print("\n======== 문제8 ========")
data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'B'])
print(data.groupby(level=0).agg(['sum', 'mean']))

# 문제 9: 가중 평균(Weighted Average) 계산
# 과목별 점수 score = pd.Series([80, 90, 70], index=['math', 'eng', 'sci'])와 
# 가중치 weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])를 활용하여
# 각 과목의 가중 점수를 합산한 최종 총점을 브로드캐스팅 연산을 통해 구하시오.
print("\n======== 문제9 ========")
score = pd.Series([80, 90, 70], index=['math', 'eng', 'sci'])
weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])
x = (score * weight).sum()
print(x)

# 문제 10: 필터링 및 인덱스 재설정 (Reset Index)
# data = pd.Series([10, 30, 20, 40], index=['a', 'b', 'c', 'd'])에서 
# 1. 값이 25보다 큰 데이터만 추출하여 새로운 Series를 만드시오.
# 2. 추출된 Series의 기존 문자 인덱스를 제거하고 0부터 시작하는 숫자 인덱스로 재설정하시오.
print("\n======== 문제10 ========")
data = pd.Series([10, 30, 20, 40], index=['a', 'b', 'c', 'd'])
new_data = data[data > 25]
y = new_data.reset_index(drop=True)
print(y)