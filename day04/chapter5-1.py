# 함수
def 함수명() :              # 함수의 정의/만들기
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

함수명()

# 매개변수 : 함수 호출/사용할 때 인자값 저장하는 변수
def func2(value, n) :
    for i in range (n):
        print(value)

func2("안녕하세요", 5)

# 가변 매개변수 : 매개변수의 개수가 변할 수 있다.
def func3(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

func3(3)

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "안녕", n=3)

def func6():
    return None

def func7():
    return

print(func6() == func7())
print(func6 == func7)

def f(x):
    return x**2 + 2*x + 1

print(f(10))

