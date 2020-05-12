"""
基本上 API 没有提供的所有功能都可以用执行 JavaScript 的方式来实现了。
"""
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
