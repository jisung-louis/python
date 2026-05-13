import pandas as pd

class StatService:
    def __init__(self):
        self.df = pd.read_csv(
            './naebupyeongga/data/books.csv',
            encoding='utf-8',
            header=0
        )
        self.df['출판년월'] = pd.to_datetime(self.df['출판년월'], format="%Y년 %m월")
        self.df['출판년'] = self.df['출판년월'].dt.year
        self.df['출판월'] = self.df['출판년월'].dt.month

    def get_stats(self):
        mean_price = round(float(self.df['가격'].mean()), 2)
        max_price = int(self.df['가격'].max())
        min_price = int(self.df['가격'].min())
        most_publish_date = str(self.df['출판년'].value_counts().index[0])
        return {
            "평균가격": mean_price,
            "최고가격": max_price,
            "최저가격": min_price,
            "최다출판연도": most_publish_date+"년"
            }


stat_service = StatService()