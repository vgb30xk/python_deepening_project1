import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()

url = 'https://flight.naver.com/'
browser.get(url)

btn = browser.find_element(By.XPATH, '//button[@title= "한 달간 안보기"]')
btn.click()

begin_data = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_data.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "27"]')))
day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()

day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//button[text() = "국내"]')))
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

search = browser.find_element(By.XPATH, '//span[text() = "항공권 검색"]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

input("종료하려면 ENTER를 누르세요")
browser.quit()