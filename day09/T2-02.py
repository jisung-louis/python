# numpy 호출
import numpy as np

# [2] 배열의 주요 속성

# .shape , 현재 배열의 크기 (튜플) 반환,  (행개수,열개수)
x = np.array( [ [1,2,3] , [4,5,6] ] )   # 2차원
print(x.shape)      # (2, 3)

# .dtype , 현재 배열 내 데이터 타입 반환
x = np.array( [ 1.0 , 2.0 , 3.0 ] )
print( x.dtype )    # float64

# .size , 현재 배열 내 모든 요소 수
x = np.array( [ [1,2,3] , [4,5,6] , [7,8,9] ] )
print( x.size )     # 9

# .ndim , 현재 배열의 차원 수
x = np.array( [1,2,3] )
print( x.ndim )     # 1
x = np.array( [ [ [1],[2] ], [ [3],[4] ] ] )
print( x.ndim )     # 3

# .flat  , 다차원 배열을 1차원으로 변환
x = np.array( [ [1,2] , [3,4] , [7,0] ] )
print( x.flat )     # [1 2 3 4 7 0]
for element in x.flat :
    print( element )

## =============

# [3] 배열의 데이터 타입
# bit 란 ? 0 또는 1 으로 이루어진 2진수
# 8bit 란 ? 0 또는 1 으로 이루어진 2진수가 8개 모이면 -> 1byte
# 즉] bit 많을수록 더 많은 자료 표현할 수 있다.

# .array( 자료 , dtype = numpy.타입명 )
x = np.array( [1, 2, 3] , dtype=np.int32)
print(x.dtype)      # int32 , 정수형 32bit , bit가 클 수록 더 많은 정보를 저장한다.
# 필요에 따라 적절하게 bit 선택한다.
x = np.array( [1.0, 2.0, 3.0] , dtype=np.float64 )
print(x.dtype)      # float64 , 실수형 , 더 큰 bit 이면 더 정밀한 오차를 최소화한다.

x = np.array( [True, False, True] , dtype=np.bool_)
print(x.dtype)      # bool , 논리형

x = np.array( ['apple', 'banana', 'cherry'] , dtype=np.bytes_)
print(x.dtype)      # 문자열을 바이트형태로 저장

# .astype( numpy.변환할타입명 )
x = np.array( [1.5, 2.3, 3.7] )
print(x.dtype)              # float64
y = x.astype( np.int32 )    # float64 -> int32
print( y )                  # [1 2 3] , int(정수형)은 소수점을 표현할 수 없으므로 소수점 잘림.