# 콜백함수 : 
def call_10_tiles(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_tiles(print_hello)


# map() , filter() 함수
# map( 함수 , 리스트 ) : 리스트의 요소를 *하나씩* 함수매개변수에 대입하여 *새로운리스트* 반환
# filter( 함수 , 리스트 ) : 리스트의 요소를 *하나씩* 함수매개변수에 대입하여 참(True)인 경우 *새로운리스트* 반환
def power(item) : 
    return item * item

def under_3(item) :
    return item < 3

list_input_a = [1,2,3,4,5]

# Java : list_input_a.stream().map( 함수 ).toList();
# JavaScript : list_input_a.map( 함수 )
# Python : map( 함수 , list_input_a )

output_a = map(power, list_input_a)
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(list(output_b))

# 제너레이터 : 함수 내부에 yield 키워드를 사용하며 next()함수를 외부에서 호출하여 yield 키워드까지 실행한다.
def test() : 
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2

test()              # 함수 호출 시 실행이 안 된다.
output = test()     # (1) 함수 반환값을 변수에 저장
a = next( output )  # (2) 함수 반환값이 저장된 변수를 next에 대입한다.
print( a )          # (3) yield 까지 실행되고 yield 반환값이 반환된다.

b = next( output )
print( b )

# c = next( output )
# print( c )




# 파일처리
# open( 파일경로 , 읽기모드 )
# 읽기모드 : w새로쓰기 a이어쓰기 r읽기모드

file = open( './day05/basic.txt' , 'w')
file.write("Hello python programming...! 안녕!!!")
file.close()

with open('./day05/basic2.txt', 'w') as file :
    file.write('안녕 파이썬 프로그래밍2')

with open('./day05/basic2.txt', 'r') as file :
    contents = file.read()

print(contents)
print(type(contents))