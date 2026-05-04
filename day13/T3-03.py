import pandas as pd

# [13] 판다스 병합 , .merge(x, y, on = '공통컬럼명', how = 'inner/outer/left/right')
df_info = pd.DataFrame({'ID': [1,2,3], 'Name' : ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2,3,4], 'Score': [88, 92, 85]})

# 두 판다스 간에 ID가 같은(교집합) 자료 병합
result = pd.merge(df_info, df_score, on='ID', how='inner')
print(df_info)
print()
print(df_score)
print()
print(result)


result = pd.merge(df_info, df_score, on='ID', how='outer')
print(result)

# [14] 판다스 합치기 , .concat( [x, y], axis=0/1, ignore_index=True) # ignore_index를 사용하며 인덱스를 0부터 새로 정렬할 수 있다
result = pd.concat( [df_info, df_score], axis=0, ignore_index=True)
print(result) # 세로 연결
result = pd.concat( [df_info, df_score], axis=1)
print(result) # 가로 연결

new_score = pd.Series([85, 90, 88], name='Score')
df_info['NewScore'] = new_score # 새로운 열에 시리즈 대입
print(df_info)

# [15] 정렬 , 
# .sort_values(by='정렬기준', ascending=True/False)
# .sort_values(by=[정렬기준], ascending=True/False)
# .sort_index(axis=-0(행)/1(열), ascending=False)
df = pd.DataFrame({
    'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
    'Age': [27, 27, 22, 32], 
    'Score': [88, 95, 85, 90]
})

# 점수 기준 내림차순
result = df.sort_values(by='Score', ascending=False)
print(result)

# 나이 기준 오름차순, 나이가 같으면 점수 기준으로 내림차순
result = df.sort_values(by=['Age', 'Score'], ascending=[True, False])
print(result)

# 열이름(axis=1) / 행이름또는행인덱스(axis=0) 내림차순으로 정렬
result = df.sort_index(axis=1, ascending=False)
print(result)

# [16] 그룹 , 
# .groupby('그룹기준')['집계기준'].집계함수()
# .groupby( ['1차그룹', '2차그룹'] )['집계기준'].집계함수()
# .groupby( ['1차그룹', '2차그룹'] )['집계기준'].agg( ['집계함수1', '집계함수2'] )
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
      'Values': [ 10,  20,  30,  40,  50,  60]
})

result = df.groupby('Category')['Values'].sum()
print(result)
result = df.groupby('Type')['Values'].mean()
print(result)
# 다중 그룹
result = df.groupby(['Category', 'Type'])['Values'].sum()
print(result)
# 다중 집계
result = df.groupby(['Category', 'Type'])['Values'].agg(['sum', 'mean', 'count'])
print(result)