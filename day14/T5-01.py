import matplotlib.pyplot as plt # 맷플롯립 (시각화)
import pandas as pd # 판다스 (데이터 표 관리)
import koreanfont # 그래프 한글 깨짐 방지
import json # json 파일 load 용도

# [1] JSON 파일에서 특정한 열("customer_data")만 가져와서 데이터프레임 구성
with open('./T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load(json_file)
df_customer = pd.DataFrame(data_json['customer_data'])
print(df_customer.head())

# [2] 데이터 분석 / 시각화
# (1) 성별 과 연령대 로 그룹화 , df.groupby( [ '그룹기준', '그룹기준' ] )
# (2) 다수통계 df.agg( { '열이름' : '함수명' } )
# (3) 여러개 그룹화할 경우에는 .reset_index() 함수 이용하여 *행번호* 붙인다.
newDf = df_customer.groupby(['성별', '연령대']).agg({'고객 수':'sum', '평균 구매 금액':'mean'}).reset_index()
print(newDf)
print(newDf['연령대'])          # 남성 여성 포함하여 중복된 연령대
print(newDf['연령대'].unique()) # 남성 여성 포함하여 중복제거된 연령대
print(newDf.groupby(['연령대']).agg({'고객 수': 'sum'}))

# 1. 연령대별(그룹) 총 고객수 세로막대그래프
# (1) plt.bar( x축값 , y축값 , color='색상명또는해시코드' )
plt.bar(
    newDf['연령대'].unique() , 
    newDf.groupby(['연령대']).agg({'고객 수': 'sum'})['고객 수'] , 
    color="#FFEA00"
) 
plt.xlabel('연령대')
plt.ylabel('고객')
plt.legend()
plt.title("연령대별 누적 고객 수")
plt.show()
# 차트확인 : 30대가 비중이 가장 크고 , 50대 고객이 가장 적다

# 2. 성별 + 연령대별(그룹) 세로막대그래프
male_data = newDf[ newDf['성별'] == '남성' ] # 남성 데이터만 추출 ( 필터링 )
female_data = newDf[ newDf['성별'] == '여성' ] # 여성 데이터만 추출 ( 필터링 )

plt.bar(
    male_data['연령대'] , 
    male_data['고객 수'] , 
    label='남성 수', 
    color="#0000FF"
)
# 만약에 겹쳐 나오는 경우 : 아래 순서로 변경할 막대에 bottom = df['열이름'] 앞으로 올릴 자료 대입한다.
plt.bar(
    female_data['연령대'] , 
    female_data['고객 수'] , 
    label='여성 수', 
    color="#FFFF00",
    # bottom=male_data['고객 수']
)
plt.xlabel('연령대')
plt.ylabel('총 고객 수')
plt.title('성별 및 연령대별 누적 고객 수')
plt.legend()
plt.show()

# 3. 연령대별(그룹) '평균 구매 금액' 가로막대그래프
# plt.barh()
plt.barh( newDf['연령대'] , newDf['평균 구매 금액'], color="#FF0000")
plt.xlabel('평균 구매 금액')
plt.ylabel('연령대')
plt.title('연령대별 평균 구매 금액')
plt.show()

# 차트 확인 : 40대가 가장 구매력이 큰 집단임을 시사, 10대가 가장 적은 구매력을 가진다
