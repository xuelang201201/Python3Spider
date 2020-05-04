from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
# <title>The Dormouse's story</title>
print(type(soup.title))
# <class 'bs4.element.Tag'>
print(soup.title.string)
# The Dormouse's story
print(soup.head)
# <head><title>The Dormouse's story</title></head>
print(soup.p)  # 只会选择第一个匹配的节点，其他的后面节点都会忽略。
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
