'''
@Created By Kiryeon

Gwangyang Maintenance Technology Department
Mechanical Technology Section

Last Edit : 2021.2.21
'''

# 날씨 앱 자동 추출
import os
import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 웹브라우저 창 안 뜨게
invisible = webdriver.ChromeOptions()
invisible.add_argument("headless")

# Run chorme webdriver
# Imply chromedriver in exe file
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, options=invisible)
else:
    driver = webdriver.Chrome("chromedriver.exe", options=invisible)
driver.get("https://www.weather.go.kr/weather/forecast/timeseries.jsp")


#### 지역 설정 ####
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
###################


# Element check
print("Element check")


def isElementPresent(address):
    try:
        driver.find_element(By.XPATH, address)
    except NoSuchElementException:
        return False
    return True


# List check
print("List check")


def isEmpty(lst):
    try:
        lst[0]
    except IndexError:
        return True
    return False


# Current Weather
print("Current Weather")


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
print("Today Waether")


def TodayWeather():
    message = []
    for i in range(1, 4):
        tdTime = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[3]/dl[{0}]/dt'.format(i))
        tdWeather = driver.find_element(
            By.XPATH, '//*[@id = "dfs-panel"]/div[2]/div[3]/dl[{0}]/dd[1]/img'.format(i))
        tdTime_txt = tdTime.text
        tdWeather_att = tdWeather.get_attribute("alt")
        # print(int(tdTime_txt[0:2]))

        # No update after 17:00 pm
        if int(tdTime_txt[0:2]) > 17:
            break
        else:
            message.append("{0} : {1}\n".format(tdTime_txt, tdWeather_att))

    # Make message
    string = ""
    if isEmpty(message):  # After 17:00
        string = "그만 일하고 퇴근하세요 휴먼\n\n"
        return string
    else:  # Before 17:00
        for i, j in enumerate(message):
            string += "{0}\n".format(message[i])

    return string


# Tomorrow weather
print("Tomorrow Waether")


def tomorrowWeather():
    for i in range(1, 8):
        tmrWeather = driver.find_element(
            By.XPATH, '//*[@id="dfs-panel"]/div[4]/table/tbody/tr[3]/td[{0}]'.format(i))
        tmrWeather_att = tmrWeather.get_attribute("title")
        if tmrWeather_att == "흐림" or tmrWeather_att == "비/눈" or tmrWeather_att == "눈":
            string = "내일 날씨 최소 흐리거나 더 안 좋음\n\n"
            break
        else:
            string = "내일 날씨 평이 혹은 준수할 것으로 예상\n\n"
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
    report.write("현재기온 : {0}\n현재풍속 : {1}\n강수상태 : {2}\n\n\n########### 시간별 날씨 예상 ############\n\n".format(
        currentWeather()[0], currentWeather()[1], currentWeather()[2]))
    report.write(TodayWeather())
    report.write("\n############ 내일 날씨 예상 ############\n\n")
    report.write(tomorrowWeather())
    report.write("\n###################################\n\n")
    report.close()


# Run Program
print("Run Program")
printWeather()

# Terminate Program
print("Terminate Program")
driver.quit()

# print("Run Program")
# while True:
#     printWeather()
#     print("반복수행중")
#     time.sleep(10)
