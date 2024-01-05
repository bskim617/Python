from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
import pandas as pd
import time

# 실행하기 위해서 필요한 패키지
# pip install selenium
# pip install pandas
# 필요한 패키지 임포트: Selenium은 웹 자동화, pandas는 데이터 처리, datetime은 시간 관련 기능, time은 시간 지연 기능을 위해 사용됩니다.

# 웹드라이버를 이용하여 Chrome 브라우저를 실행하고, 인스타그램 웹사이트를 엽니다. time.sleep(3)은 페이지 로딩을 위해 3초간 대기합니다.
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(3)

# 로그인
driver.find_element(By.NAME, 'username').send_keys("jay187.5")  # ID 입력
time.sleep(5)
driver.find_element(By.NAME, 'password').send_keys("a157674!")  # PW 입력
time.sleep(5)
# driver.find_element(By.NAME, 'username').send_keys("seongju_shuiiing")  # ID 입력
# time.sleep(5)
# driver.find_element(By.NAME, 'password').send_keys("insta1Rkdy$%^&")  # PW 입력
# time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(3)

# 특정 사용자 페이지로 이동
keywords = ["busanunnie"]
profile_url = f"https://www.instagram.com/{keywords[0]}/"
driver.get(profile_url)
time.sleep(8)

# 좋아요를 누른 사용자들을 저장할 딕셔너리를 초기화합니다.
liked_users = {}

for i in range(1, 7):
	# 1부터 6까지 반복하여 각 게시물에 대해 처리합니다.
	try:
		# 게시물이 위치한 행과 열을 계산합니다.
		row_index = 1 if i <= 3 else 2
		post_index = i if i <= 3 else i - 3

		# 각 게시물의 링크를 찾고, 해당 게시물의 고유 ID를 추출합니다.	
		post_link = driver.find_element(By.CSS_SELECTOR, f"article > div:nth-child(1) > div > div:nth-child({row_index}) > div:nth-child({post_index}) > a")
		post_href = post_link.get_attribute("href")
		post_id = post_href.split("/")[-2]
	except NoSuchElementException:
		# 게시물을 찾지 못할 경우 오류 메시지를 출력하고 다음 게시물로 넘어갑니다.
		print(f"게시물 {i}를 찾을 수 없습니다")
		continue

	# 추출한 게시물 ID를 사용하여 좋아요 목록 페이지로 이동합니다.
	driver.get(f"https://www.instagram.com/p/{post_id}/liked_by/")
	time.sleep(8)

	while True:
		try:
			# 좋아요 목록이 모두 로드될 때까지 스크롤을 내리며 사용자 이름을 수집합니다.
			likes_elements = driver.find_elements(By.CSS_SELECTOR,"a > div > span > div")
			for element in likes_elements:
				username = element.text
				if username:
					if username not in liked_users:
						liked_users[username] = [0] * 6
					liked_users[username][i-1] = 1
					# 각 사용자의 이름을 추출하여 liked_users 딕셔너리에 저장합니다.
			
			# 페이지 끝까지 스크롤합니다.
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(5)

			 # 더 이상 새로운 좋아요 사용자가 로드되지 않으면 반복을 종료합니다.
			new_likes_elements = driver.find_elements(By.CSS_SELECTOR,"a > div > span > div")
			if len(new_likes_elements) <= len(likes_elements):
				break
		except Exception as e:
			# 오류 발생 시 메시지를 출력하고 다음 게시물로 넘어갑니다.
			print(f"게시물 {i}의 좋아요 사용자를 가져오는 도중 오류가 발생했습니다: {e}")
			break
	
	# 프로필 페이지로 돌아갑니다.
	driver.get(profile_url)
	time.sleep(8)

# pandas DataFrame을 사용하여 liked_users 딕셔너리를 데이터프레임으로 변환합니다.
df_likes = pd.DataFrame.from_dict(liked_users, orient='index', columns=[f'게시글{j}' for j in range(1, 7)])

# 각 사용자별로 좋아요 합계를 계산하고, 합계에 따라 데이터프레임을 정렬합니다.
df_likes['합계'] = df_likes.sum(axis=1)
df_sorted = df_likes.sort_values(by='합계', ascending=False)

# 현재 시간을 파일 이름에 포함시켜 저장합니다
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"data/insta_liked_users_{current_time}.xlsx"

# 엑셀 파일로 저장합니다. 시트 이름은 키워드로 지정합니다.
sheet_name = keywords[0] if keywords else 'Sheet1'
df_sorted.to_excel(file_name, index_label='user_id', sheet_name=sheet_name)

# 브라우저 종료
# 웹드라이버를 종료합니다.
driver.quit()