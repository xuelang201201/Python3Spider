from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://book.douban.com/')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'book.douban.com', 'value': 'charlie'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
