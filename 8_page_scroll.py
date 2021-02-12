'''
어차피 자동화 프로그램인데 스크롤 내릴 일이 어디 있다고 이걸 쓰냐고 생각하면,
페이지 전체를 한 번 로딩해서 불러온 상태로 모든 데이터를 다 받은 상태가 되니까
그걸 이용할 수 있음
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(
    "C:/Users/St_Marcellinus/Desktop/RPA/chromedriver_88.exe")

browser.get("https://shopping.naver.com/home/p/index.nhn")

# 무선마우스 입력
browser.find_element(
    By.XPATH, '//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")

# 검색버튼
browser.find_element(By.XPATH, '//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤

# 1. 지정한 위치로 스크롤 내리기 (자바스크립트 문법을 이용하는 방법)
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1080)')


# 2. 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight')


# 3. 동적 페이지에 대해 마지막까지 스크롤 반복 내리기
interval = 2  # 2초에 한 번씩 스크롤 내리려고
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 반복수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기(위에 정의한 시간)
    time.sleep(interval)
    # 현재 문서높이 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:  # 직전 높이와 같으면, 즉, 높이의 변화가 없으면
        break  # 반복문 탈출 (모든 스크롤 동작 완료)
    prev_height = curr_height

# 다시 맨 위로 올리기
browser.execute_script("window.scrollTo(0,0)")

time.sleep(3)
