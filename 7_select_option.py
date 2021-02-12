# 웹페이지 DropDown, 엑셀 Combo Box
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(
    "C:/Users/Be Irreplaceable/Desktop/RPA/3_web/chromedriver.exe")
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

# cars에 해당하는 element를 찾고, dropdown 내부 4번째 옵션 선택
# index 값을 이용해 option을 선택하는 방법
browser.switch_to.frame("iframeResult")
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[2]')
# option[i] : i번째 항목
elem.click()

time.sleep(3)

# 텍스트 값을 이용해 option을 선택하는 방법
# 옵션중에서 텍스트가 Audi인 항목을 선택
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
elem.click()

time.sleep(3)

# 텍스트 값이 부분일치하는 항목 선택 방법 (위에는 완전일치의 조건이었음)
elem = browser.find_element(
    By.XPATH, '//*[@id="cars"]/option[contains(text(), "Vol")]')
elem.click()

time.sleep(3)
