from selenium import webdriver
from selenium.webdriver.common.by import By

"""1.获取属性"""
browser = webdriver.Chrome()
url = 'https://book.douban.com/'
browser.get(url)
nav = browser.find_element_by_id('db-nav-book')
print(nav)
print(nav.get_attribute('class'))
browser.close()

"""2.获取文本值"""
browser = webdriver.Chrome()
url = 'https://book.douban.com/'
browser.get(url)
logo = browser.find_element_by_class_name('nav-logo')
print(logo.text)
browser.close()

"""3.获取 id、位置、标签名和大小"""
browser = webdriver.Chrome()
url = 'https://book.douban.com/'
browser.get(url)
input_ = browser.find_element_by_class_name('nav-logo')
print(input_.id)
print(input_.location)
print(input_.tag_name)
print(input_.size)
browser.close()
