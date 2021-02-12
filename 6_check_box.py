from selenium import webdriver
from selenium.webdriver.common.by import By  # element문 길게 쓰기 싫을 때 사용
import time
browser = webdriver.Chrome(
    "C:/Users/Be Irreplaceable/Desktop/RPA/3_web/chromedriver.exe")

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame("iframeResult")

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')

# button과 달리 check box는 반복클릭에 따라 선택이 될 수도 풀릴 수도 있으니
# 반드시 클릭해야 하는 상황의 경우 꼭 if문으로 분기하여 처리하는 게 좋다.
if elem.is_selected() == False:
    print("선택 안 되어 있으므로 선택")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안함")

time.sleep(3)
