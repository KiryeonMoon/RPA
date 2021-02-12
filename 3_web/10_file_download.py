import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 크롬 다운로드의 주 디렉토리인 "다운로드" 디렉토리 말고
# 디렉토리 위치를 내가 원하는 곳으로 지정해줌
chrome_options = Options()
chrome_options.add_experimental_option(
    'prefs', {'download.default_directory': r'C:\Users\St_Marcellinus\Desktop\RPA'})

browser = webdriver.Chrome(
    "C:/Users/St_Marcellinus/Desktop/RPA/chromedriver_88.exe", options=chrome_options)
browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
browser.switch_to.frame("iframeResult")
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(3)
