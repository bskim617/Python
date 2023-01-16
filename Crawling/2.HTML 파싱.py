"""
이름 : 김보성
날짜 : 2023/01/16
내용 : 파이썬 HTML 파싱 실습하기
"""
import requests as req
from bs4 import BeautifulSoup as bs

# HTML 요청
url = 'http://chhak.click/parsing/sample2.html'
html = req.get(url).text
print(html)

# 문서객체 생성
dom = bs(html, 'html.parser')

# 문서파싱
tit = dom.html.body.h1.text
txt = dom.select_one('p').text
lis = dom.select('ul > li')

print('tit :', tit)
print('txt :', txt)

for li in lis:
    print('li text :', li.text)

