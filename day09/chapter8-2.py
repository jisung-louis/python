class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스와 __init__() 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init__() 메소드가 호출되었습니다.")

child = Child()
child.test()
print(child.value)