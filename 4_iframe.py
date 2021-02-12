import time
from selenium import webdriver

browser = webdriver.Chrome(
    "C:/Users/Be Irreplaceable/Desktop/RPA/3_web/chromedriver.exe")
browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# 브라우저 속 iframeResult라는 name을 가진 iframe으로 전환
browser.switch_to.frame("iframeResult")

elem = browser.find_element_by_xpath('//*[@id="male"]')

elem.click()

# 작업을 마치고 다시 상위 frame으로 빠져나옴
browser.switch_to.default_content()

time.sleep(5)  # 밑에 quit 명령 실행 전 5초 대기 명령

# browser.quit()
