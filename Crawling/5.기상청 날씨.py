"""
날짜 : 2023/01/18
이름 : 김보성
내용 : 파이썬 기상청 날씨 정보 크롤링 실습하기
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

# 가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 기상청 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 전국 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

# 출력
# for tr in trs:
#    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
#    print(tds[0].text)

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                       user='root', 
                       passwd='1234', 
                       db='java1db', 
                       charset='utf8')
# SQL 실행객체
cur = conn.cursor()

# 조건문 
for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    var = []
    for j in tds:
        if j.text == ' ':
            var.append(None)
        else:
            var.append(j.text)

        # SQL 실행
        sql = "insert into `weather` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    cur.execute(sql, var)
    conn.commit()

# 가상 브라우저 종료
print('등록 완료...')
conn.close()
browser.close()
print('프로그램 종료...')
