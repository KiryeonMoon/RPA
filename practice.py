# 날씨 앱 자동 추출
import schedule
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 웹드라이버 호출
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.weather.go.kr/weather/forecast/timeseries.jsp")

#### 지역 설정 ####
driver.find_element(
    By.XPATH, '//*[@id="content_weather"]/div[2]/dl/dd/a[1]/img').click()  # 동네찾기
time.sleep(0.25)
driver.find_element(
    By.XPATH, '//*[@id="localTbody"]/ul/li[13]/a').click()  # 전라남도
time.sleep(0.25)
driver.find_element(
    By.XPATH, '//*[@id="localTbody"]/ul/li[5]/a').click()  # 광양시
time.sleep(0.25)
driver.find_element(By.LINK_TEXT, '금호동').click()  # 금호동
 time.sleep(0.25)
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
    ###################

## 현재 기상정보 ##
nowTemp = driver.find_element(
    By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[1]').text  # 현재 온도, 기온
nowWind = driver.find_element(
    By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[2]').text  # 현재 풍속
# nowWind = driver.find_element(By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[3]').text # 습도 불필요하므로 제외
nowRain = driver.find_element(
    By.XPATH, '//*[@id="dfs-panel"]/div[2]/div[2]/dl/dd[4]').text  # 현재 강수량

# 출력


def printWeather():
    # print("현재기온 : {0}\n현재풍속 : {1}\n강수상태 : {2}".format(nowTemp, nowWind, nowRain))
    print("A")

# schedule.every(10).seconds.do(printWeather) # 10분마다 실행

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# time.sleep(10)
# now = time.localtime()
# print(now.tm_sec)

# while True:
#     if now.tm_sec != 0:
#         print(now.tm_sec)
#         time.sleep(1)
#         continue
#     print("현재기온 : {0}\n현재풍속 : {1}\n강수상태 : {2}".format(nowTemp, nowWind, nowRain))


schedule.every(10).seconds.do(printWeather)

while True:
    schedule.run_pending()
    time.sleep(1)
