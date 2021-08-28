from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import datetime

driver = webdriver.Chrome()
url = 'https://vnexpress.net/covid-19/covid-19-viet-nam'
driver.get(url)
def getDB():
    source = BeautifulSoup(driver.page_source,'html.parser')
    total_case = driver.find_element_by_class_name('total_case')
    today_case = driver.find_element_by_xpath('/html/body/section[4]/div/div[2]/div[2]/strong')
    number_item_khoi = driver.find_element_by_xpath('//*[@id="total-all"]/div[2]/span[1]')
    number_item_tuvong = driver.find_element_by_xpath('//*[@id="total-all"]/div[3]/span[1]')
    number_item_dangdieutri = driver.find_element_by_xpath('//*[@id="total-all"]/div[4]/span[1]')

    total_case = float(total_case.text)
    today_case = float(today_case.text)
    number_item_tuvong = float(number_item_tuvong.text)
    number_item_khoi = float(number_item_khoi.text)
    number_item_dangdieutri = float(number_item_dangdieutri.text)

    while total_case % 1 != 0:
        total_case = total_case * 10
    total_case = int(total_case)
    while today_case % 1 != 0:
        today_case = today_case * 10
    today_case = int(today_case)
    while number_item_tuvong % 1 != 0:
        number_item_tuvong = number_item_tuvong * 10
    number_item_tuvong = int(number_item_tuvong)
    while number_item_khoi % 1 != 0:
        number_item_khoi = number_item_khoi * 10
    number_item_khoi = int(number_item_khoi)
    while number_item_dangdieutri % 1 != 0:
        number_item_dangdieutri = number_item_dangdieutri * 10
    number_item_dangdieutri = int(number_item_dangdieutri)

    db = [(total_case,today_case,number_item_khoi,number_item_tuvong,number_item_khoi,datetime.date.today())]
    print(db)
    return db

if __name__ == '__main__':
    getDB()
    driver.close()
