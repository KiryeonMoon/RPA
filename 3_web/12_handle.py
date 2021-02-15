# 운영체제가 무언가를 식별하기 위한 key값 개념
# 브라우저가 뜰 때마다 브라우저 창별로 handle 번호를 부여함
import time
from selenium import webdriver

browser = webdriver.Chrome(
    "C:/Users/St_Marcellinus/Desktop/RPA/chromedriver_88.exe")

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

# 이 사이트 핸들 가져오는거
curr_handle = browser.current_window_handle
print(curr_handle)  # 현재 윈도우 핸들정보 출력

# try yourself 버튼 클릭 >> 새 창이 뜰 거임
browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles  # 모든 핸들 정보
for handle in handles:
    print(handle)  # 각 핸들정보 출력
    browser.switch_to.window(handle)  # 각 핸들로 이동해서
    print(browser.title)  # 해당 핸들(브라우저)의 제목 출력
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행..

# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()

print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)
print(browser.title)

# 브라우저 컨트롤이 가능한지 확인
time.sleep(3)
browser.get("http://naver.com")

time.sleep(3)
