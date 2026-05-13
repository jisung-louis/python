import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


all_book_data = []

# 크롤링
for page_num in range(1, 10):
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page_num}&pageSize=120&viewMode=list'
    print(f">>>현재 {page_num} 페이지 수집 중 : {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select("#yesBestList>li")
    
    for book in books:
        title_tag = book.select_one(".gd_name")
        price_tag = book.select_one(".yes_b")
        salecount_tag = book.select_one(".saleNum")
        publishdate_tag = book.select_one(".info_date")
        # print("[TITLE TAG] : ", title_tag)
        # print("[PRICE TAG] : ", price_tag)
        # print("[SALECOUNT TAG] : ", salecount_tag)
        # print("[PUBLISHDATE TAG] : ", publishdate_tag)
        # print()
        title = title_tag.get_text().strip()
        price = int(price_tag.get_text().strip().replace(",",""))
        salecount = int(salecount_tag.get_text().strip().replace("판매지수 ","").replace(",",""))
        publishdate = publishdate_tag.get_text().strip()
        # print("[TITLE] : ", title)
        # print("[PRICE] : ", price)
        # print("[SALECOUNT] : ", salecount)
        # print("[PUBLISHDATE] : ", publishdate)
        # print()
        all_book_data.append({
            "도서 제목": title,
            "가격": price,
            "판매지수": salecount,
            "출판년월": publishdate
        })
        print(f"  책 제목 : {title}")
    time.sleep(1)
print("모든 수집 완료")

# 리스트를 DataFrame으로 
df = pd.DataFrame(all_book_data, columns=["도서 제목", "가격", "판매지수", "출판년월"])
df.info()

# 데이터 export
df.to_csv(
    './naebupyeongga/data/books.csv',
    index=False,
    encoding='utf-8-sig',
    na_rep='Unknown',
    header=True
)

# 수집 대상
# 1. 도서 제목
# 2. 가격
# 3. 판매지수
# 4. 출판년월