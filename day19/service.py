# 서비스 클래스
import pandas as pd

class ItemService : 
    # 생성자
    def __init__(self):
        self.df = pd.DataFrame([
            {'id': 1, 'name': '콜라', 'price': 10000},
            {'id': 2, 'name': '콜라', 'price': 10000}
        ])
    # 함수
    # (1) 개별 조회 식 서비스
    def item(self, id):
        # df[조건식]    # df[df['특정열'] == 값]
        result = self.df[self.df['id'] == id]
        if result.empty : 
            return "해당 상품이 없습니다"
        
        # df 타입 대신에 .to_json() 또는 .to_dict
        print(result) # df 조회 결과가 하나라도 항상 *리스트* 형식
        return result.to_dict(orient='records')

    def items(self):
        return self.df.to_dict(orient='records')
    
    def save(self, item):
        # 1. 저장할 객체를 데이터프레임으로 만든다
        saveDf = pd.DataFrame( [item] )
        # 2. 기존 데이터프레임에 연결한다.
        self.df = pd.concat([self.df , saveDf], ignore_index=True)
        return self.df.to_dict(orient='records')

    def update(self, item):
        # 1. 수정할 id가 df에 존재 여부 확인
        update_id = item.get('id')
        if update_id not in self.df['id'].values:
            return "수정할 상품이 없습니다."
        # 2. 해당 수정할 Id에 index찾기
        idx = self.df[self.df['id'] == update_id].index
        # 3. 찾은 index에 값 수정
        self.df.loc[idx, item.keys()] = item.values()
        # 4.
        return True

    def delete(self, id):
        # 1. 삭제할 id 가 df에 존재 여부 확인
        if id not in self.df['id'].values:
            return '삭제할 상품이 없습니다'
        # 2. 삭제할 id 제외한 df 재구성
        self.df = self.df[self.df['id'] != id]
        # 3.
        return True
# ** 서비스 객체 생성 **
item_service = ItemService()