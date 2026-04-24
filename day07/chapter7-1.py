# 모듈 호출 하기
# 표준 모듈 : 파이썬 내장 라이브러리 
# 외부 모듈 : 설치형 라이브러리
# import 모듈명

import math
import random

pi = 3.14159265

for i in range(16 + 1):
    x = pi * i / 8
    print(f"{x:.5f}", f"{math.sin(x):.2f}")

print()
print(random.random())
print(random.uniform(10,20))        # uniform(시작값, 끝값) , 실수
print(random.randrange(1,10))       # randrange(시작값, 끝값) , 정수
print(random.choice([10,24,5,20]))  # choice([리스트]) , 리스트 내 랜덤 요소 1개 반환
a = [1,2,3,4,5]
print(random.shuffle(a))
print(a)
print(random.sample([1,2,3,4,5], k=2))  # sample([리스트], k=개수) , 리스트 내 k개 랜덤 요소 반환
