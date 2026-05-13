import pandas as pd
import matplotlib.pyplot as plt
import json
import koreanfont

# [1] T5_data.json 파일내 'risk_return_data'
with open( './T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['risk_return_data'])

# [2] 산점도 : 리스크 대비 수익률
plt.scatter(df['리스크'], df['수익률(%)'], s=df['수익률(%)']*100, alpha=0.5)
plt.xlabel('리스크')
plt.ylabel('수익률')
plt.title('리스크 대비 수익률')
plt.show()

# [3] 산점도 : 자산별 리스크 대비 수익률
categories = df['자산'].unique()    # unique : 중복제거
print(categories)
for i , category in enumerate(categories):
    sub = df[df['자산'] == category]    # 동일한 자산 정보 가져오기
    print(sub)
    plt.scatter(sub['리스크'] , sub['수익률(%)'] , label=category)
    
plt.legend()
plt.show()