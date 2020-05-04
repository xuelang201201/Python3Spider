from bs4 import BeautifulSoup

"""子节点和子孙节点
"""
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
# ['\n    Once upon a time there were three little sisters; and their names were\n    ',
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>, '\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, '\n
# and\n', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, '\n
# and they lived at the bottom of a well.\n']

print(soup.p.children)
# <list_iterator object at 0x7f4dee5da370>
for i, child in enumerate(soup.p.children):
    print(i, child)
# 0
#     Once upon a time there were three little sisters; and their names were
#
# 1 <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# 2
#
# 3 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 4
# and
#
# 5 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 6
# and they lived at the bottom of a well.

print(soup.p.descendants)
# <generator object Tag.descendants at 0x7fed16f07f90>
for i, child in enumerate(soup.p.descendants):  # descendants 会递归查询所有子节点，得到所有的子孙节点。
    print(i, child)
# 0
#     Once upon a time there were three little sisters; and their names were
#
# 1 <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# 2
#
# 3 <span>Elsie</span>
# 4 Elsie
# 5
#
# 6
#
# 7 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 8 Lacie
# 9
# and
#
# 10 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 11 Tillie
# 12
# and they lived at the bottom of a well.


"""父节点和祖先节点
"""
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)
# <p class="story">
#             Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>

html = """
<html>
<body>
<p class="story">
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(type(soup.a.parents))
# <class 'generator'>
print(list(enumerate(soup.a.parents)))  # a节点的祖先节点
# [(0, <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>), (1, <body>
# <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# </body>), (2, <html>
# <body>
# <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# </body></html>), (3, <html>
# <body>
# <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# </body></html>)]


"""兄弟节点
"""
html = """
<html>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
            Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Sibling', list(enumerate(soup.a.next_siblings)))
print('Prev Sibling', list(enumerate(soup.a.previous_siblings)))
# Next Sibling
#             Hello
#
# Prev Sibling
#             Once upon a time there were three little sisters; and their names were
#
# Next Sibling [(0, '\n            Hello\n'), (1, <a class="sister" href="http://example.com/lacie" id="link2">
#   Lacie</a>), (2, '\n            and\n'), (3, <a class="sister" href="http://example.com/tillie" id="link3">
#   Tillie</a>), (4, '\n            and they lived at the bottom of a well.\n')]
# Prev Sibling [(0, '\n            Once upon a time there were three little sisters; and their names were\n')]


"""提取信息
"""
html = """
<html>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
class="sister" id="link2">Lacie</a>
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
# Next Sibling:
# <class 'bs4.element.Tag'>
print(soup.a.next_sibling)
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
print(soup.a.next_sibling.string)
# Lacie
print('Parent:')
print(type(soup.a.parents))
# Parent:
# <class 'generator'>
print(list(soup.a.parents)[0])
# <p class="story">
#             Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">Bob</a><a class="sister"
# href="http://example.com/lacie" id="link2">Lacie</a>
# </p>
print(list(soup.a.parents)[0].attrs['class'])
# ['story']
