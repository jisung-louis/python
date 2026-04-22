# 피보나치 수열 (메모화)

dictionary = {
    1 : 1 ,
    2 : 1
}

def func4(n) :
    if n in dictionary : # 만약에 n(매개변수값)이 딕셔너리에 존재하면
        return dictionary[n] # 메모(저장)된 값을 리턴
    else :
        output = func4(n - 1) + func4(n - 2)
        dictionary[n] = output
        return output

print(func4(20))