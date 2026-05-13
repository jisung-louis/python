import pandas as pd
import matplotlib.pyplot as plt
import json
import koreanfont

# [1] T5_data.json 파일내 'financial_performance_data'
with open( './T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load(json_file)
df = pd.DataFrame(data_json['financial_performance_data'])

# [2] 플롯박스 : '수익' '비용' '이익' 으로 박스플롯 표시

# [3] 플롯박스 : 분기별 수익 데이터 로 박스플롯 표시
