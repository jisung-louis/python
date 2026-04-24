# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 
#       - 로그인
#       - 로그아웃
#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력

# === 로그인 세션 ===
session = {}
no = 0

# === 회원가입 메소드 ===
def signup_view():
    # 1. ID, PW 입력받기
    id_input = input("아이디 입력 : ")
    pw_input = input("비밀번호 입력 : ")
    
    # 2. 존재하는 아이디인지 확인
    with open("./day08/users.txt", "r") as file:
        is_already_exists = False
        for account in file:
            global no
            (no, id, pw) = account.strip().split(", ")
            no = int(no)
            if id == id_input:
                is_already_exists = True

        if is_already_exists:
            print(f"'{id}'는 이미 존재하는 아이디입니다.")
            return

    # 3. 파일(users.txt) 저장
    with open("./day08/users.txt", "a") as file:
        file.write(f"{no + 1}, {id_input}, {pw_input}\n")

    # 5. 끝
    print(f"{id_input} 아이디로 회원가입이 완료되었습니다.")
    return

# === 로그인 메소드 ===
def login_view():
    # 1. ID, PW 입력받기
    id_input = input("아이디 입력 : ")
    pw_input = input("비밀번호 입력 : ")

    with open("./day08/users.txt", "r") as file:
        for account in file:
            (no, id, pw) = account.strip().split(", ")
            if id == id_input and pw == pw_input:
                session["id"] = id
                session["pw"] = pw
                print(f"{id} 계정으로 로그인에 성공했습니다.")
                return

    if len(session) == 0:
        print("아이디 또는 비밀번호가 올바르지 않습니다.")
    return

# === 로그아웃 메소드 ===
def logout_view():
    del session["id"]
    del session["pw"]
    print("로그아웃이 완료되었습니다.")
    return

# === 지역명 검색 ===
def search_by_district_name_view():
    district = input("검색할 시군구를 입력하세요 : ")
    with open("./day08/data.csv", "r", encoding="euc-kr") as file:
        for line in file:
            lst = line.strip().split('","')
            lst[0] = lst[0].replace('"', '')
            lst[-1] = lst[-1].replace('"', '')
            if len(lst) == 1:
                continue
            if lst[0] == "NO":
                continue

            if district in lst[1]:
                print(lst)

# === 금액 범위 검색 ===
def search_by_price_range_view():
    min_price = int(input("검색할 최소 금액을 입력하세요(만원 단위) : "))
    max_price = int(input("검색할 최대 금액을 입력하세요(만원 단위) : "))
    with open("./day08/data.csv", "r", encoding="euc-kr") as file:
        for line in file:
            lst = line.strip().split('","')
            lst[0] = lst[0].replace('"', '')
            lst[-1] = lst[-1].replace('"', '')
            if len(lst) == 1:
                continue
            if lst[0] == "NO":
                continue

            price = int(lst[9].replace(',',''))
            if min_price <= price <= max_price:
                print(lst)


# === 전체 통계 조회 ===
def find_all_statistics_view():
    sum = 0
    count = 0
    max_price = 0
    min_price = 10000000000
    with open("./day08/data.csv", "r", encoding="euc-kr") as file:
        for line in file:
            lst = line.strip().split('","')
            lst[0] = lst[0].replace('"', '')
            lst[-1] = lst[-1].replace('"', '')
            if len(lst) == 1:
                continue
            if lst[0] == "NO":
                continue

            price = int(lst[9].replace(',',''))
            sum += price
            count += 1

            if price > max_price:
                max_price = price
            
            if price < min_price:
                min_price = price
    print(f"[평균 거래가] : 약 {(sum // count)} 만 원")
    print(f"[최고 거래가] : {max_price} 만 원")
    print(f"[최저 거래가] : {min_price} 만 원")

# === 메인 ===
while True:
    print("\n==== 경기도 아파트 실거래가 조회 시스템 ====")
    if len(session) == 0:
        print("(1) 회원가입 || (2) 로그인")
    else:
        print("(1) 지역명 검색 || (2) 금액 범위 검색 || (3) 전체 통계 조회 || (4) 로그아웃")
    
    ch = input("입력 > ")
    
    if ch == '1':
        if len(session) == 0:
            signup_view() # 회원가입
        else:
            search_by_district_name_view() # 지역명 검색

    elif ch == '2':
        if len(session) == 0:
            login_view() # 로그인
        else:
            search_by_price_range_view() # 금액 범위 검색

    elif ch == '3':
        if len(session) == 0:
            break
        else:
            find_all_statistics_view() # 전체 통계 조회

    elif ch == '4':
        if len(session) == 0:
            break
        else:
            logout_view() # 로그아웃

    else:
        break



