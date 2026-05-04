import pandas as pd

# 판다스 # pd.Series # 1차원 # pd.DataFrame # 2차원

# [1] 데이터프레임 생성 , pd.DataFrame( 2차원리스트 , columns = [ 열이름 ] , index = [ 행이름 ] )
data_list = [ 
    ['Ant' , 25 , 'Seoul'], 
    ['Bee', 30, 'Busan'], 
    ['Cat', 35, 'Incheon'] ]

x = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print( x )

# [2] 데이터프레임 생성2 , pd.DataFrame( 딕셔너리 ) , 대부분의 공공자료는 *딕셔너리*
data_dict = {
    'Name': ['Ant', 'Bee', 'Cat'],
    'Age': [25, 30, 35],
    'City': ['Seoul', 'Busan', 'Incheon']
}
x = pd.DataFrame(data_dict)
print(x)

# [3] 데이터프레임 생성3 , pd.DataFrame( 넘파이배열 , columns = [ 열이름 ] , index = [ 행이름 ] )
import numpy as np
data_np = np.array(data_list)
x = pd.DataFrame(data_np, columns=['Name', 'Age', 'City'], index=['a', 'b', 'c'])   # column -> 칼럼 이름 , # index -> 행 이름
print(x)

# [4-1] 주요 속성
print(x.shape)      # (3, 3) 행/열 크기
print(x.columns)    # 칼럼 목록
print(x.index)      # 인덱스 목록
print(x.values)     # 값만 2차원 으로 반환

# [4-2] 주요 탐색
print(x.head(2))    # 상위 n개 만 반환 (주로 확인용으로 씀)
print(x.tail(2))    # 하위 n개 만 반환 (주로 확인용으로 씀)
x.info()            # 전처리(데이터 정리) 하기 전 결측치/타입 *확인*

# [5] 인덱싱
print(x.iloc[1])    # iloc[인덱스번호]
print(x.iloc[1, 2]) # iloc[행, 열]
print(x.loc['a'])   # loc[라벨명]
print(x.loc['b', 'City']) # loc[라벨명, 컬럼명]

#  [6] 슬라이싱 , [시작인덱스 : 끝인덱스]
print(x.iloc[0:2, 0:1])                 # [행슬라이싱 , 열슬라이싱]
print(x.loc['a':'b', 'Name': 'Age'])    # [행슬라이싱 , 열슬라이싱]

# [7] 새로운 열 추가 , ['새로운 열'] = 새로운 값 , .assign( 새로운 열 = 새로운 값 )
x['Score'] = [100, 80, 95]      # 파괴적 (원본 수정))
print(x)

x = x.assign(Score2 = [87, 65, 78]) # 비파괴적 (새로운 판다스 변환)
print(x)

# [8] 특정한 값 수정 , [기존열읾]
x['Age'] = [31, 52, 40]
print(x)

x['b', 'Age']  = 70     # b 행의 age 열 값을 70 으로 변경
print(x)

x.iloc[0, 0] = 'apple'   # 0행의 0열 값을 'apple'으로 변경/수정
print(x)

# 여러개 한 번에 수정 , 
# loc [ [ 수정할라벨 , 수정할라벨] , 수정컬럼라벨 ] = [ 새로운값 ]
# iloc [ [ 수정할인덱스 , 수정할인덱스] , 수정컬럼인덱스 ] = [ 새로운값 ]
x.loc[ ['a', 'b'], 'Score' ] = [10, 20]
print(x)

# [9] 필터링 , x[ 조건식 ] , x [ x[열이름] > y ]
cont1 = x['Score2'] > 70
print( cont1 )          # True , False , True
print(x[cont1])         # 데이터프레임[조건]

cont2 = x['Age'] > 35   # 2번째 조건
print(x[cont1 & cont2]) # 1번째 조건 과 2번째 조건으로 논리연산
print(x[cont1 | cont2])

# [10] 필터링 조건으로 새로운 열 추가 또는 수정
x.loc[ x['Score2'] > 70, 'passed'] = True       # 열 추가
x.loc[ x['Score2'] <= 70, 'passed'] = False     # 열 수정
print(x)


# [11] 열(칼럼) 이름 수정 , .rename( index={} , columns= { 'old' : 'new' } )
x = x.rename(columns={ 'City' : '도시', 'Age': '나이'})
print(x)

# [12] 집계 , .describe() : 수치자료들을 집계 요약, # x[ 열이름 ].집계함수()
print(x.describe())
print(x['나이'].sum())  
print(x['Score'].mean())
print(x['passed'].value_counts()) # 특정 열의 빈도 확인