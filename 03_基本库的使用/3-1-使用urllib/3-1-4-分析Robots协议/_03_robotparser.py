"""解析 robots.txt"""

from urllib.robotparser import RobotFileParser
from urllib.request import urlopen


def set_url():  # 通过 set_url() 方法设置 robots.txt 的链接。
    rp = RobotFileParser()
    rp.set_url('http://www.bilibili.com/robots.txt')
    rp.read()
    # 使用 can_fetch() 方法判断网页是否可以被抓取。
    print(rp.can_fetch('*', 'http://www.bilibili.com/vide/BV15J411T7WQ'))
    print(rp.can_fetch('*', 'http://www.bilibili.com/search?q=python&page=1&type=collections'))


def parse():  # 使用 parse() 方法执行读取和分析
    rp = RobotFileParser()
    rp.parse(urlopen('http://www.bilibili.com/robots.txt').read().decode('utf-8').split('\n'))
    print(rp.can_fetch('*', 'http://www.bilibili.com/vide/BV15J411T7WQ'))
    print(rp.can_fetch('*', 'http://www.bilibili.com/search?q=python&page=1&type=collections'))


if __name__ == '__main__':
    set_url()
    parse()
