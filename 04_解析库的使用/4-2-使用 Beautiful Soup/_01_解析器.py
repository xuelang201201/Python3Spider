"""lxml 解析器有解析 HTML 和 XML 的功能，而且速度快，容错能力强"""
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)
