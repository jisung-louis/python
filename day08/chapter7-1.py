# OS 모듈
import os

print(os.name)      # nt : 윈도우 뜻
print(os.getcwd())  # 현재 최상위 폴더
print(os.listdir()) # 현재 최상위 폴더의 내부 요소
os.mkdir('hello')   # 폴더 생성
os.rmdir('hello')   # 폴더 삭제
with open('./day08/original.txt', 'w') as file:
    file.write('hello')
os.rename('./day08/original.txt', './day08/new.txt')    # 파일명 변경
os.remove('./day08/new.txt')    # 파일 삭제
# os.system('ifconfig')

import datetime

print(datetime.datetime.now())
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

output_a = now.strftime('%Y-%m-%d %H:%M:%S')
print(output_a)

# 시간 계산
output = now.replace(year=(now.year + 1) , month = (now.month - 1))
print(output)

# time 모듈
import time
print('3초간 일시정지')
time.sleep(3)       # 3초간 일시정지    # 스레드 일시정지, 스레드란? 코드가 실행되는 흐름단위
print('땡')

# urllib 모듈
# from urllib import request  # from 이용하여 특정한 함수/변수 만 가져오기
# target = request.urlopen( "https://skuri.kr" )
# output = target.read()

# print(output)

from operator import itemgetter
books = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
},{
    "제목": "혼자 공부하는 머신러닝",
    "가격": 28000
},{
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 12000
}]

print("cheapest")
print(min(books, key=itemgetter("가격")))
print(max(books, key=itemgetter("가격")))

