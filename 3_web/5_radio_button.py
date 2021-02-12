import time
from selenium import webdriver

browser = webdriver.Chrome(
    "C:/Users/Be Irreplaceable/Desktop/RPA/3_web/chromedriver.exe")
# browser.maximize_window() # 실행시 창 최대화
browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame("iframeResult")
elem = browser.find_element_by_xpath('//*[@id="male"]')

# 체크 안되어있으면 선택하기
if elem.is_selected() == False:
    print(("선택 안되어 있으니 선택"))
    elem.click()
else:
    print("선택되어 있으니 아무것도 안함")

time.sleep(5)
