from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(
    "C:/Users/Be Irreplaceable/Desktop/forGitHub/chromedriver.exe")
browser.get("http://naver.com")
emt = browser.find_element_by_id("query")

portfolio = [
    "삼성전자",
    "SK하이닉스",
    "포스코",
    "현대자동차",
    "LG화학"
]

price = []


for i, j in enumerate(portfolio):
    if i == 0:
        emt.send_keys("{0} 주식정보".format(j))
        emt.send_keys(Keys.ENTER)
        price.append(browser.find_element_by_xpath(
            '//*[@id="_cs_root"]/div[1]/div/h3/a/span[2]/strong').text)
    else:
        emt = browser.find_element_by_id("nx_query")
        emt.clear()
        emt.send_keys("{0} 주식정보".format(j))
        emt.send_keys(Keys.ENTER)
        price.append(browser.find_element_by_xpath(
            '//*[@id="_cs_root"]/div[1]/div/h3/a/span[2]/strong').text)

print("오늘 주가는 이러하다.")
for i, j in enumerate(price):
    print("{0} 주가 : {1}원".format(portfolio[i], j))
