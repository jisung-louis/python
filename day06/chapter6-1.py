# 예외처리  에외가 발생할 상황을 예측하고 모두 조건문으로 처리하는 것은 매우 힘들다.
# 예외가 발생하면 프로그램이 강제로 종료되지 않게 흐름 제어 하기 = 예외처리 
# try: ~ except: ~

try:
    int(input('정수 입력 : '))

# except(ValueError):
#     print("정수만 입력하세요")

except(Exception):
    print("정수만 입력하라고")

list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        print(f"어! \"{item}\"은(는) 문자열인데!")
        pass
    else:
        print(f"헤헤, \"{item}\"라는 숫자가 들어왔잖아.")

print(f"{list_input_a} 내부에 있는 숫자는")
print(f"{list_number} 입니다")

# finally : (예외가 있든 없든) 무조건 실행할 코드
try: 
    pass
except:
    print("정수를 입력하세요.")
else:
    print("예외가 발생하지 않았다")
finally:
    print("무조건 실행되는 코드")