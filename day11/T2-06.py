import numpy as np

# 통계
x = np.array( [1,2,3,4,5] )

print( np.min(x) )
print( np.max(x) )
print( np.argmin(x) )   # 최솟값 위치(인덱스)
print( np.argmax(x) )   # 최댓값 위치(인덱스)
print( np.ptp(x) )      # 최댓값 - 최솟값
print( np.sum(x) )      # 합계
print( np.mean(x) )     # 평균
print( np.median(x) )   # 중앙값
print( np.var(x) )      # 분산 : 요소들의 흩어짐 정도
print( np.std(x) )      # 표준편차 : 분산의 양의 제곱근
print( np.sqrt(x) )     # 루트

# 사분위수 ,
q1 = np.percentile( x , 25 )    # 1/4 , 25% , 하위 25%
q3 = np.percentile( x , 75 )    # 3/4 , 75% , 하위 75%
print( q1 )
print( q3 )
q2 = np.percentile( x , 50 )    # 2/4 , 50% , 중앙값
print( q2 )

q4 = q3 - q1
print(q4)

# 2차원 배열 통계 , 통계함수(x , axis = 0)  2차원에서 axis=0 : 열기준 axis=1 : 행기준, axis 생략하면 평탄화해서 나옴
y = np.array( [[1,2,3], [4,5,6]] )
print(np.min(y, axis= 0))   # 열 개수가 3개 이니까 최솟값 3개
print(np.min(y, axis= 1))   # 행 개수가 2개 이니까 최솟값 2개
print(np.min(y))            # axis 생략하면 2차원배열 평탄화(1차원으로변경)해서 통계
print(np.argmax(y))
print(np.argmin(y))
print(np.sum(y, axis=0))