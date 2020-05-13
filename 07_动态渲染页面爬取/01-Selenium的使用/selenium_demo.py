import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def demo():
    """Selenium 的基本使用"""
    try:
        browser.get('https://www.baidu.com')
        input_ = browser.find_element_by_id('kw')
        input_.send_keys('Python')
        input_.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()


def get_page():
    """访问页面"""
    browser.get('https://www.taobao.com')
    print(browser.page_source)
    browser.close()


def get_element():
    """查找单个节点"""
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id('q')
    # input_first = browser.find_element(By.ID, 'q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third)
    browser.close()


def get_elements():
    """查找多个节点"""
    browser.get('https://www.taobao.com')
    lis = browser.find_element_by_css_selector('.service-bd li')
    # lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
    print(lis)
    browser.close()


def elements_interaction():
    """节点交互"""
    browser.get('https://www.taobao.com')
    input_ = browser.find_element_by_id('q')
    input_.send_keys('iPhone')
    time.sleep(1)
    input_.clear()
    input_.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()


def action_chains():
    """动作链"""
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()


def execute_javascript():
    """执行JavaScript"""
    browser.get('https://book.douban.com')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')


def get_element_infos():
    """获取节点信息"""

    """1.获取属性"""
    url = 'https://book.douban.com'
    browser.get(url)
    nav = browser.find_element_by_id('db-nav-book')
    print(nav)
    print(nav.get_attribute('class'))
    browser.close()

    """2.获取文本值"""
    url = 'https://book.douban.com'
    browser.get(url)
    logo = browser.find_element_by_class_name('nav-logo')
    print(logo.text)
    browser.close()

    """3.获取 id、位置、标签名和大小"""
    url = 'https://book.douban.com'
    browser.get(url)
    input_ = browser.find_element_by_class_name('nav-logo')
    print(input_.id)
    print(input_.location)
    print(input_.tag_name)
    print(input_.size)


def switch_to_frame():
    """切换 Frame"""
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)


def waiting():
    """延时等待"""

    """1.隐式等待"""
    browser.implicitly_wait(10)
    browser.get('https://book.douban.com')
    input_ = browser.find_element_by_class_name('nav-logo')
    print(input_)

    """2.显式等待"""
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    input_ = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input_, button)


def forward_back():
    """前进和后退"""
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.bilibili.com/')
    browser.back()
    time.sleep(1)
    browser.forward()
    browser.close()


def cookies():
    """使用 Selenium，可以对 Cookies 进行获取、添加、删除等操作。"""
    browser.get('https://book.douban.com')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'book.douban.com', 'value': 'charlie'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


def window_tabs():
    """选项卡管理"""
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://python.org')


def handle_exceptions():
    """异常处理"""
    try:
        browser.get('https://www.baidu.com')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('hello')
    except NoSuchElementException:
        print('No Element')
    finally:
        browser.close()


def main():
    # demo()
    # get_page()
    # get_element()
    # get_elements()
    # elements_interaction()
    # action_chains()
    execute_javascript()
    # get_element_infos()
    # switch_to_frame()
    # waiting()
    # forward_back()
    # cookies()
    # window_tabs()
    # handle_exceptions()


if __name__ == "__main__":
    browser = webdriver.Chrome()  # 不要放在方法里面，否则Chrome会闪退
    main()
