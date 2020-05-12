from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""1.隐式等待"""
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://book.douban.com/')
input_ = browser.find_element_by_class_name('nav-logo')
print(input_)

"""2.显式等待：效果比隐式等待更好"""
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input_ = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input_, button)
