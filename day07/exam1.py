# 예외객체 : Exception 클래스
# 1] try ~ except 에외클래스명 as 변수명 ~ except 예외클래스명 as 변수명
# 2] 모든 예외 잡기 : *마지막에 except에 Exception 클래스 사용한다
# 3] 강제 에외 발생 : 1) 미구현 2) 웹/앱 프레임워크(유효성검사/트랜잭션 등)


list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print(f"{number_input}번째 요소 : {list_number[number_input]}")
    raise NotImplementedError
except ValueError as e:
    print("정수만 입력하세요.", e)
except IndexError as e:
    print("인덱스를 벗어났어요.", e)
except NotImplementedError as e:
    print("아직 구현되지 않음", e)
except Exception as e:
    print("type(exception):", type(e))
    print("exception:", e)