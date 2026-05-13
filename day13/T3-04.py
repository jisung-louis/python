# [1] 맷플롯립 설치 : uv pip install matplotlib
# [2] 맷플롯립 불러오기 : import matplotlib

import matplotlib as mpl
# print(mpl.__version__)

# # 차트 내 한글 꺠짐 방지 코드( + 한글 폰트 )
mpl.rc('font', family='AppleGothic')        # 한글 폰트 설정
mpl.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지

# [3] 관례적 import
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# [1] 선 그래프
import matplotlib.pyplot as plt

# 1. 그래프의 데이터 준비
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # x축( 가로축 의 값 )
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # y축( 세로축 의 값 )

# 2. 그래프 설정
plt.plot(x, y)
plt.title('Line Chart Exam')    # .title('차트제목')
plt.xlabel('X-axis Title')      # .xlabel('x축제목')
plt.ylabel('Y축')      # .ylabel('y축제목')
plt.grid(True)

# 3. 그래프 출력
plt.show()

# [2] 선 그래프2
y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     # 
plt.plot(x, y, label='감소하는 선(항목명)', color='blue', linestyle=':')
plt.plot(x, y2, label='증가하는 선(항목명)', color="#FF0000", linestyle='-')
plt.legend()

plt.show()

# [3] 막대 그래프
categories = ['학생1', '학생2', '학생3', '학생4']
values     = [80    , 92    , 78    , 90    ]
values2    = [88    , 91    , 75    , 85    ]

# 막대 겹치지 않게 표시
import numpy as np
x = np.arange(len(categories))  # 0부터 x축의 값 개수 만큼 생성  0 ~ 3

plt.bar(x - 0.2, values, width=0.4, label='국어성적', color='blue')
plt.bar(x + 0.2, values2, width=0.4, label='수학성적', color='red')
plt.title('학생 성적 비교')
plt.xlabel('학생명')
plt.ylabel('성적점수')
plt.legend()
plt.grid(axis='y')
plt.xticks(x, categories)   # 위치 순으로 라벨 지정

plt.show()

# [4] 파이 그래프 , 백분율 , .pie( 값, labels = ['항목명'], colors='색상', explode='강조(튀어나오는정도)', startangle='시작각도', autopct='비율표시')
labels = ['피자', '햄버거', '샐러드', '파스타']
sizes  = [40   , 30    , 20     , 10    ]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = [0.1, 0, 0, 0]

plt.pie(sizes, labels=labels, colors=colors, explode=explode, startangle=90, autopct='%1.1f%%') 
# %형식문자 : %자릿수.소수자릿수f , %% 퍼센트('%')를 표시하기 위한 방법

plt.title('음식 선호도')
plt.legend()

plt.show()

# [5] 산점도 , 밀집도 , .scatter(x축값, y축값, c(color) = '색상', s=점크기)
x = [1.5, 2.5, 3.5, 4.5, 5.5]
y = [50, 60, 65, 70, 75]

plt.scatter(x, y, c='red', s=100) # color -> c로 줄임 가능 , sizes -> s로 줄임 가능
plt.grid()

plt.show()

# [6] 히스토그램 , 상관관계 , .hist( 값 , color='' , alpha=투명도 , bins=구간개수 )
data = []
for i in range(50):
    value = sum([ (i * j) % 100 / 100 for j in range(1, 13) ])   # 리스트 내포 ( 1차원 리스트 생성 )
    # (i*j) % 100 : 나머지값 계산
    # /100 : 0 ~ 1 사이 값으로 계산
    # sum() : 총합계 , 즉] 13개의 0~1 사이의 난수를 만ㄷ르어서 총합계 ( 중앙값이 큰 난수 생성될 예정 )
    data.append( value )

print(data)

# 차트 만들기
plt.hist( data , color='skyblue', alpha=0.5, bins=30)
plt.show()

# [7] 다중 그래프 구현 , .subplot( 행개수 , 열개수 , figsize = ( 가로 , 세로 ) )
fig, axs = plt.subplots(1, 2, figsize=( 10 , 7 ))    # 한 줄에 2개 차트
# fig : 다중 그래프를 가지고 있는 전체 그래프
# axs : 다중 그래프의 위치, axs[0] 첫번쨰 그래프 , axs[1] 두번째 그래프
# figsize = ( 가로 , 세로 ) , 전체 그래프의 가로inch , 세로inch
axs[0].plot( [1,2,3], [1,4,9] )
axs[0].set_title('선 그래프')       # 주의할점 : .title() : 전체 그래프의 제목 , .set_title() : 하위 그래프의 제목
axs[0].set_xlabel('x축 제목')       # 즉] .title , xlabel , ylabel 등 에서는 set_XXXX() 으로 사용하기
axs[0].set_ylabel('y축 제목')       

axs[1].bar( [1,2,3], [3,5,2] )
axs[1].set_title('막대그래프')
axs[1].set_xlabel('x축제목')
axs[1].set_ylabel('y축제목')

plt.savefig('./day13/save_chart.png')   # 그래프 이미지(png) 다운로드 , .savefig('파일경로')

plt.show()

fig, axs = plt.subplots( 2 , 2 )  # 행=2, 열=2, 총 그래프 수 = 4
axs[0][0].plot()
axs[0][1].bar()
axs[1][0].scatter()
axs[1][1].pie()