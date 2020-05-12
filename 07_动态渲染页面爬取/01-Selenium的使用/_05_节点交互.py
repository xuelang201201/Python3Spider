import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_ = browser.find_element_by_id('q')
input_.send_keys('iPhone')
time.sleep(1)
input_.clear()
input_.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
