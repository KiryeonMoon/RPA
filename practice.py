'''
Created By Kiryeon

Gwangyang Maintenance Technology Department
Mechanical Technology Section
'''

# # 패키지 설치여부 확인 및 설치 함수
# import subprocess
# import sys

# print("Check if package is installed")
# def install_pkg(package):
#     try:
#         __import__(package)
#         print(" ", package, ": already installed")
#     except ImportError:
#         subprocess.call([sys.executable, "-m", "pip", "install", "--trusted-host=files.pythonhosted.org", "--trusted-host=pypi.org", package])
#         print("", package, " successly installed")

# # 패키지 설치
# print("Install Packages")
# install_pkg("time")
# install_pkg("selenium")

# # chrome webdriver 설치여부 확인
# print("Check if webdriver is installed")
# import os

# check = os.path.isfile("C/Users/POSCOUSER/chromedriver.exe")
# if not check:
#     import requests
#     import zipfile
#     url = "https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/chromedriver_win32.zip"
#     r = requests.get(url, allow_redirects=True, verify=False)
#     open("C/Users/POSCOUSER/chromedriver_win32.zip", "wb").write(r.content)
#     zipfile.ZipFile("C/Users/POSCOUSER/chromedriver_win32.zip").extractall("C:\\Users\POSCOUSER\\")
#     print(" ", "chromedriver installed")
# else:
#     print(" ", "already installed")


# 날씨 앱 자동 추출
import sys
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 웹브라우저 창 안 뜨게
invisible = webdriver.ChromeOptions()
invisible.add_argument("headless")

# Chrome webdriver 호출
# webdriver 가상경로 추가
if getattr(sys, "frozen", False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, options=invisible)
else:
    driver = webdriver.Chrome(
        "C:/Users/Be Irreplaceable/Desktop/forGitHub/chromedriver.exe", options=invisible)

driver.get("https://www.weather.go.kr/weather/forecast/timeseries.jsp")

# 지역 설정 #########d
driver.find_element(
    By.XPATH, '//*[@id="content_weather"]/div[2]/dl/dd/a[1]/img').click()  # 동네찾기
time.sleep(0.5)
driver.find_element(
    By.XPATH, '//*[@id="localTbody"]/ul/li[13]/a').click()  # 전라남도
time.sleep(0.5)
driver.find_element(
    By.XPATH, '//*[@id="localTbody"]/ul/li[5]/a').click()  # 광양시
time.sleep(0.5)
driver.find_element(By.LINK_TEXT, '금호동').click()  # 금호동
time.sleep(0.5)
driver.find_element(
    By.XPATH, '//*[@id="layor_area"]/form/fieldset/p/a[1]/img').click()  # 관심지역 등록

# alert창 처리
try:
    result = driver.switch_to_alert()
    result.accept()
    print(result)
except:
    pass

time.sleep(3)
driver.find_element(
    By.XPATH, '//*[@id="layor_area"]/p/a/img').click()  # 설정 완료된 창 닫기

time.sleep(3)
driver.find_element(
    By.XPATH, '//*[@id="content_weather"]/div[1]/dl/dd/form/input').click()  # 변경하기
###########################

# Element check


def isElementPresent(address):
    try:
        driver.find_element(By.XPATH, address)
    except NoSuchElementException:
        return False
    return True

# Current Weather


def currentWeather():
    if isElementPresent('//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[5]'):  # 강수 있을 경우
        nowTemp = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[2]').text  # 현재 온도 및 기온
        nowWind = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[3]').text  # 현재 풍속
        nowRain = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[5]').text  # 현재 강수량
    else:  # 강수 없을 경우
        nowTemp = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[1]').text  # 현재 온도, 기온
        nowWind = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[2]').text  # 현재 풍속
        nowRain = "비/눈 없음"

    return [nowTemp, nowWind, nowRain]

# Today weather


def TodayWeather():
    for i ~~~
    //*[@id = "dfs-panel"]/div[2]/div[3]/dl[i]/dd[1]/img


# Tomorrow weather
def tomorrowWeather():
    for i in range(1, 8):
        tmrWeather = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[4]/table/tbody/tr[3]/td[{0}]'.format(i))
        tmrWeather_att = tmrWeather.get_attribute("title")
        if tmrWeather_att == "흐림" or tmrWeather_att == "비/눈" or tmrWeather_att == "눈":
            string = "내일 날씨 최소 흐리거나 더 안 좋음. 드론 날기 힘듦\n\n"
            break
        else:
            string = "내일 날씨 평이 혹은 준수할 것으로 기대됨. 추이를 지켜봐야 할 듯\n\n"
    return string


# Weather Info Function
print("Weather Info Function")


def printWeather():

    # Current Time
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min

    # Make text
    report = open("C:/Users/Be Irreplaceable/Desktop/Report.txt", "w")
    report.write(
        "####### 최근 업데이트 : {0}시 {1}분 #########\n\n".format(hour, minute))
    report.write("현재기온 : {0}\n현재풍속 : {1}\n강수상태 : {2}\n\n\n############ 내일 날씨 예상 ############\n\n".format(
        currentWeather()[0], currentWeather()[1], currentWeather()[2]))
    report.write(tomorrowWeather())
    report.write("###################################")
    report.close()


# Run Program
print("Run Program")
while True:
    printWeather()
    print("반복수행중")
    time.sleep(10)
