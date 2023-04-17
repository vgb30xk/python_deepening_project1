import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 2. 조회 항목 초기화
checkboxes = browser.find_elements(By.NAME, "fieldIds")
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


# 3. 조회 항목 설정
items_to_select = ['시가', '고가', '저가']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, "..")
    label = parent.find_element(By.TAG_NAME, "label")
    if label.text in items_to_select:
        checkbox.click()

# 4. 적용하기 클릭
btn_apply = browser.find_element(
    By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 45):
    # 페이지 이동
    browser.get(url + str(idx))

    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break

    # 6. 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name):
        df.to_csv(f_name, encoding='utf-8-sig',
                  index=False, mode='a', header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)

    print(f'{idx} 페이지 완료')

browser.quit()
