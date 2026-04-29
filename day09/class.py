# 객체 : 속성(상태) 과 메소드(행동) 로 이루어진 추상화 :: 논리적인 개념
# 클래스 : 객체를 프로그래밍에서 표현하기 위한 설계도
# 인스턴스 : 클래스 기반으로 생성한 객체 :: 물리적인 개념
# 생성자 : 인스턴스가 생성될 떄 실행되는 함수 = 초기화함수 역할

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("윤인성1", 87, 98, 88, 95), # 인스턴스 생성 , Java : new 클래스명( 인자값 ) vs Python : 클래스명( 인자값 )
    Student("윤인성2", 87, 98, 88, 95),
    Student("윤인성3", 87, 98, 88, 95),
    Student("윤인성4", 87, 98, 88, 95),
    Student("윤인성5", 87, 98, 88, 95),
]