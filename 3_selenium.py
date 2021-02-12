from selenium import webdriver

# 이 브라우저를 핸들링할 수 있는 변수 선언
browser = webdriver.Chrome("./chromedriver.exe")

# get : 이 url로 이동한다는 명령어
browser.get("http://daum.net")
