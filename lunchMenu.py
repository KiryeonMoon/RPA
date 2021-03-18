import sys
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common import keys

# 크롬 웹드라이버
driver = webdriver.Chrome("./chromedriver.exe")

# poswel 창 켜기
driver.get("http://poswel.co.kr")
driver.maximize_window()
time.sleep(3)

# 주간메뉴 클릭
driver.find_element_by_xpath('//*[@id="tm1"]/li[10]/a').click()
time.sleep(3)


def find_target(img_file, timeout):
    start = time.time()  # start time
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file, confidence=0.9)
        print("찾는중")
        end = time.time()
        if end-start > timeout:
            break
    return target


def my_click(img_file, timeout):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(
            f"[Timeout {timeout}s] Target not found ({img_file}) Terminate program.")
        sys.exit()


# 광양 클릭
my_click("kwangyangButton.png", 10)
# driver.find_element_by_xpath(
#     '//*[@id="todaymenu"]/ul/li/ul/li[2]/button').click()


# # 그린식당 클릭
my_click("greenButton.png", 10)
# driver.find_element_by_xpath(
#     '//*[@id="todaymenu"]/ul/li/ul/li[2]/button').click()

# time.sleep(10)

# iframe 진입
driver.switch_to.frame("cboxIframe")

menuList = []
for i in range(0, 5):
    for j in range(0, 3):
        menu = driver.find_element_by_xpath(
            '//*[@id="list_3day"]/div[{0}]/div[2]/div/div[2]/span[1]'.format(i))
        print(menu)
        menuList.append(menu)
    driver.find_element_by_xpath('//*[@id="list_arrow_left"]/a/img').click()
    time.sleep(1)

# iframe 탈출
driver.switch_to_default_content()
time.sleep(5)

print("[프로그램 종료]")

# for i, j in enumerate(iframes):
#     try:
#         driver.switch_to.frame(j[i])
#         print(driver.page_source)
#         driver.switch_to_default_content()
#     except:
#         driver.switch_to_default_content()
#         print("pass by except : iframe[{0}]".format(i))
#         pass
