from selenium import webdriver

proxy = '120.79.139.253:8080'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(options=options)
browser.get('http://httpbin.org/get')
