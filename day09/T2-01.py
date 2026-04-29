# (1) numpy 이란? 고성능 수치 계산 라이브러리
# (2) 설치 : 터미널에서 'pip install numpy'
# (3) numpy 불러오기 : import numpy
import numpy

# .zeros( (행, 열) ) , 행 과 열 만큼의 0 으로
x = numpy.zeros( (2, 3) )
print( x )
# [[0. 0. 0.]
#  [0. 0. 0.]]

# .ones( (행, 열) ) , 행 과 열 만큼의 1 으로 배열 초기화
x = numpy.ones( (2, 3) )
print( x )
# [[1. 1. 1.]
#  [1. 1. 1.]]

# .full( (행, 열), 값 ) , 행 과 열 만큼의 값으로 배열 초기화
x = numpy.full( (2, 3), 10 )
print( x )
# [[10 10 10]
#  [10 10 10]]

# .arange( 시작, 끝 , 단위 ) , 시작부터 끝 단위만큼 증가한 배열
x = numpy.arange(0, 10, 2)
print( x )
# [0 2 4 6 8]

# .linspace( 시작 , 끝 , 개수 ) , 시작 부터 끝 사이의 개수만큼 균등하게 
x = numpy.linspace(0, 1, 5)
print( x )
# [0.   0.25 0.5  0.75 1.  ]