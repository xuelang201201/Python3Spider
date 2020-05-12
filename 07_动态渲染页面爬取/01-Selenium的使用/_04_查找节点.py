from selenium import webdriver
from selenium.webdriver.common.by import By

"""1.单个节点"""
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
# input_first = browser.find_element(By.ID, 'q')  # 也可以使用 find_element() 方法
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()

"""2.多个节点"""
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')  # 也可以使用 find_elements() 方法
print(lis)
browser.close()
