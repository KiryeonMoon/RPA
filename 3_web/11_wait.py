# 로딩하는동안 기다려야 하는 상황
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩 대기를 위한 임포트
from selenium.webdriver.support import expected_conditions as EC  # 예상되는 조건


browser = webdriver.Chrome(
    "C:/Users/St_Marcellinus/Desktop/RPA/chromedriver_88.exe")
browser.get("https://flight.naver.com/flights/")

# 가는 날 클릭
browser.find_element(By.LINK_TEXT, '가는날 선택').click()
browser.find_element(
    By.XPATH, '//*[@id="l_8"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/a').click()
# 바로 이어서 오는날 클릭
browser.find_element(
    By.XPATH, '//*[@id="l_8"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[3]/td[4]/a').click()

# 제주도 클릭
browser.find_element_by_xpath(
    '//*[@id="recommendationList"]/ul/li[1]/div/span').click()

# 항공권 검색 클릭
browser.find_element_by_xpath('//*[@id="searchArea"]/a').click()

# 기다리는 방법 1 : 타임슬립 걸어서 로딩 될때까지 한 10초 기다려주면 됨
# time.sleep(10)  # 불필요한 시간낭비 발생. 비효율적

# 기다리는 방법 2 : 결과 element가 나올 때까지 기다리는 방법. try except 사용
try:
    # 예상되는 조건(EC)으로 element가 존재할(element_located) 때까지(until) 10초동안 기다린다.(webdriverWait)
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[2]')))
    # 10초 안에 결과가 나오면 바로 다음 문장으로 넘어간다.
    print(elem.text)
except:
    # 출력에 실패했으면,
    print("실패했소")

# 결과 출력
# elem = browser.find_element_by_xpath(
#     '//*[@id="content"]/div[2]/div/div[4]/ul/li[2]').click()
# print(elem.text)

time.sleep(2)
