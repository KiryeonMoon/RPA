# 페이지 내부에 메인 스크롤 말고 별도로 존재하는 스크롤 조절
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(
    "C:/Users/St_Marcellinus/Desktop/RPA/chromedriver_88.exe")
browser.get("https://www.w3schools.com/html/default.asp")
browser.maximize_window()

# 특정 영역 스크롤 방법
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[61]')

# # 1. Actionchain 사용
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 2. 좌표정보 이용
xy = elem.location_once_scrolled_into_view  # 함수가 아닌 변수라서 괄호 안쓰고 그대로 씀
print("type : ", type(xy))  # dict
print("value : ", xy)

elem.click()

time.sleep(3)
