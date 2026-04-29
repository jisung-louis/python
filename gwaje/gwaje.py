import numpy as np
from numpy.char import upper
data = np.genfromtxt("./gwaje/data.csv", delimiter=',', skip_header=1, encoding='utf-8', dtype=str)

# Step 4: 진학률 상위 학교/학과 분석 (Statistics & Sorting)

# 미션: 대학원 진학 등 취업 대신 학업을 이어가는 비율이 높은 학교/학과를 찾기 위해, 진학률이 가장 높은 학교/학과를 추출하세요. 
# 분석 결과: 진학률 1위 학교/학과 (                )  ,  진학률: (                ) %
# 의미: 해당 학과의 학생들이 취업보다 학업 연장이나 전문성 강화를 선택하는 경향이 강한지 확인할 수 있습니다. 
# 진학률이 높은 학과는 연구직, 전문직, 대학원 진학과 관련된 진로 특성이 강할 가능성이 있습니다.

is_upper_30 = data[:, 15].astype(int) >= 30 # '졸업자_계'가 30명 이상인지
is_university = data[:, 1] == "대학"
upper_30 = data[is_upper_30 & is_university] # '졸업자_계'가 30명 이상, "대학"인 행

jinhak_rate = upper_30[:, 45].astype(float)
max_index = np.argmax(jinhak_rate)
print('학교/학과명 : ', upper_30[max_index, 2] + ' ' + upper_30[max_index, 13], '|| 진학률 : ', jinhak_rate[max_index])


# Step 5: 취업준비생 비율 분석 (Broadcasting & Ratio Calculation)

# 미션: 졸업자 수에서 취업자 수, 진학자 수, 취업불가능자 수를 제외하여 취업준비생 수를 계산하고, 취업준비생 비율이 가장 높은 학과를 찾으세요. 
# (취업준비생 수 = 졸업자 수 - 취업자 수 - 진학자 수 - 취업불가능자 수)

# 분석 결과: 취업준비생 비율이 70% 이상인 학교/학과 (    )  ,  취업준비생 비율: (   ) %
# 의미: 졸업 후 취업도, 진학도 하지 않은 학생의 비율을 확인하여 실질적인 취업 지원이 필요한 학과를 찾을 수 있습니다. 

# 이 비율이 높은 학과는 취업 준비 장기화, 진로 미결정, 취업 지원 부족 등의 문제가 있을 가능성이 있습니다.

# 졸업자 수가 30명 이상인 학과만 가져온다
# "졸업자_계" 칼럼 인덱스 : 15
print()

is_upper_30 = data[:, 15].astype(int) >= 30 # '졸업자_계'가 30명 이상인지
is_university = data[:, 1] == "대학"
upper_30 = data[is_upper_30 & is_university] # '졸업자_계'가 30명 이상, "대학"인 행

graduate = upper_30[:, 15].astype(int) # upper_30 행들의 졸업생 수
employed = upper_30[:, 21].astype(int) # upper_30 행들의 취업자 수
student = upper_30[:, 48].astype(int) # upper_30 행들의 진학자 수
enlistee = upper_30[:, 51].astype(int) # upper_30 행들의 입대자 수
impossible = upper_30[:, 52].astype(int) # upper_30 행들의 취업불가능자 수
foreigner = upper_30[:, 55].astype(int) # upper_30 행들의 외국인유학생 수
excluded = upper_30[:, 58].astype(int) # upper_30 행들의 제외인정자 수
etc = upper_30[:, 52].astype(int) # upper_30 행들의 기타 수
unknown = upper_30[:, 52].astype(int) # upper_30 행들의 미상 수

job_seeker = graduate - employed - student - enlistee - impossible - foreigner - excluded - etc - unknown
job_seeker_percentage = job_seeker / graduate

baeksu = upper_30[job_seeker_percentage > 0.7]
baeksu_univ = baeksu[:,2]
baeksu_dept = baeksu[:,13]
baeksu_percentage = job_seeker_percentage[job_seeker_percentage > 0.7]

baeksu_grad = graduate[job_seeker_percentage > 0.7]
baeksu_js = job_seeker[job_seeker_percentage > 0.7]

print("[취업준비생 비율이 70% 이상인 학교/학과]")
for i in range(len(baeksu_dept)):
    print(f"{baeksu_univ[i]} {baeksu_dept[i]} || 비율 : {baeksu_percentage[i] * 100:.2f}% || 졸업자 수 : {baeksu_grad[i]}명 || 취업준비생 수 : {baeksu_js[i]}명")

