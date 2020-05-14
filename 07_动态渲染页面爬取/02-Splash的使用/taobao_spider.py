import pymongo
import time
import requests

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
from selenium.webdriver import ActionChains

KEYWORD = '华为'
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'productions'
MAX_PAGE = 100

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def try_login():
    """尝试登录"""
    try:

        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)

        login = browser.find_element_by_id('fm-login-id')
        login.clear()
        login.send_keys('username')
        time.sleep(1)
        password = browser.find_element_by_id('fm-login-password')
        password.clear()
        password.send_keys('password')
        time.sleep(1)

        source = browser.find_element_by_id('nc_1_n1z')
        # target = browser.find_element_by_id('nc_1_n1t')
        actions = ActionChains(browser)
        # actions.drag_and_drop(source, target)
        actions.drag_and_drop_by_offset(source, 258, 0)
        actions.perform()
        time.sleep(1.5)

        button = browser.find_element_by_class_name('fm-btn')
        button.click()
        time.sleep(1)

        print("登录成功")
    except Exception as reason:
        print("登录失败：" + str(reason))


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:

        if page > 1:
            input_ = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            '#mainsrp-pager div.form > span.btn.J_Submit')))
            input_.clear()
            input_.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'),
                                             str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存到 MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert_one(result):
            print('存储到 MongoDB 成功')
    except Exception as reason:
        print('存储到 MongoDB 失败: ' + str(reason))


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    try_login()
    main()
